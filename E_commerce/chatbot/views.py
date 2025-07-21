from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from langchain_community.chat_models import ChatOllama
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from .tools import get_all_products, get_product_details, get_products_in_category, get_all_categories
from .models import ChatHistory

# Initialize the LLM
llm = ChatOllama(model="qwen2.5-coder:1.5b")

# Define a custom prompt template
custom_prompt = PromptTemplate.from_template("""
Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action (always a JSON object for structured tools)
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

When the user asks about a product, first consider if they might be referring to a category with the same name. If a product name is ambiguous (e.g., 'mouse' could be a product or a category), try to search for it as a category first using `get_products_in_category`, then as a product using `get_product_details` if no category is found. Always provide a clear, concise final answer to the user.

If the user asks a basic greeting (e.g., "hello", "hi", "how are you"), respond appropriately without using any tools.

If the user asks for information that is not related to products, categories, or general greetings, or if they ask for sensitive information such as user details, passwords, or other private data, respond with: "Hey, I am only here to help you with your shopping."

Begin!

Question: {input}
Thought:{agent_scratchpad}
""")

# Initialize the agent
tools = [get_all_products, get_product_details, get_products_in_category, get_all_categories]
agent = create_react_agent(llm, tools, custom_prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

@login_required
def chat(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        
        # Save user message to history
        ChatHistory.objects.create(user=request.user, message=user_input, is_user_message=True)
        
        # Pre-process user input for greetings and irrelevant questions
        user_input_lower = user_input.lower()
        if any(greeting in user_input_lower for greeting in ["hello", "hi", "hey", "how are you"]):
            response = "Hello! How can I assist you with your shopping today?"
        elif "capital of" in user_input_lower or \
             "who is" in user_input_lower or \
             "what is" in user_input_lower and "product" not in user_input_lower and "category" not in user_input_lower or \
             "when was" in user_input_lower or \
             "where is" in user_input_lower:
            response = "Hey, I am only here to help you with your shopping."
        else:
            # Get the response from the LLM using invoke()
            try:
                agent_output = agent_executor.invoke({"input": user_input})
                response = agent_output.get("output", "I'm sorry, I couldn't process that request.")
            except Exception as e:
                response = f"An error occurred: {e}"
        
        # Save bot response to history
        ChatHistory.objects.create(user=request.user, message=response, is_user_message=False)
        
        return JsonResponse({'response': response})
    
    chat_history = ChatHistory.objects.filter(user=request.user).order_by('timestamp')
    return render(request, 'chatbot/chat.html', {'chat_history': chat_history})
