from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from langchain_ollama import ChatOllama
from .models import ChatHistory
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import PromptTemplate

# Initialize the LLM
llm = ChatOllama(model="qwen2.5-coder:1.5b")

db = SQLDatabase.from_uri("sqlite:///db.sqlite3")

# Define a custom prompt template
custom_prompt = PromptTemplate.from_template("""
Given an input question, first create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.
Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per {dialect}.
You can order the results by a relevant column to return the most interesting examples in the database.
Never query for all columns from a table. You must query only the columns that are needed to answer the question.
Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist.
Also, pay attention to which column is in which table.

Use the following format:

Question: "Question here"
SQLQuery: "SQL Query to run"
SQLResult: "Result of the SQLQuery"
Answer: "Final answer here"

Only use the following tables:
{table_info}

If the user asks about a product, first consider if they might be referring to a category with the same name. If a product name is ambiguous (e.g., 'mouse' could be a product or a category), try to search for it as a category first, then as a product if no category is found. If the user asks for the price of a product, make sure to query the `selling_price` column. Always provide a clear, concise final answer to the user.

If the user asks for information that is not related to products, categories, or general greetings, or if they ask for sensitive information such as user details, passwords, or other private data, respond with: "Hey, I am only here to help you with your shopping."

Question: {input}
""")

db_chain = SQLDatabaseChain.from_llm(llm, db, prompt=custom_prompt, verbose=True)

@login_required
def chat(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        
        # Save user message to history
        ChatHistory.objects.create(user=request.user, message=user_input, is_user_message=True)
        
        # Pre-process user input for greetings and sensitive questions
        user_input_lower = user_input.lower()
        user_info_keywords = ["user", "profile", "account", "password", "email", "address", "phone", "full_name", "zip_code", "city", "country"]

        if any(greeting in user_input_lower for greeting in ["hello", "hi", "hey", "how are you"]):
            response = "Hello! How can I assist you with your shopping today?"
        elif any(keyword in user_input_lower for keyword in user_info_keywords):
            response = "For privacy reasons, I cannot answer questions about user information."
        else:
            # Get the response from the LLM using the db_chain
            try:
                response = db_chain.run(user_input)
            except Exception as e:
                response = f"An error occurred: {e}"
        
        # Save bot response to history
        ChatHistory.objects.create(user=request.user, message=response, is_user_message=False)
        
        return JsonResponse({'response': response})
    
    chat_history = ChatHistory.objects.filter(user=request.user).order_by('timestamp')
    return render(request, 'chatbot/chat.html', {'chat_history': chat_history})
