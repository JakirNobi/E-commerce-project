from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
from langchain.prompts import PromptTemplate
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_openai import ChatOpenAI
import os
import logging

from .models import ChatHistory

# Set up logging
logger = logging.getLogger(__name__)

# Initialize the LLM with OpenRouter and Qwen3 model in chat mode
llm = ChatOpenAI(
    model="qwen/qwen3-235b-a22b:free",  # Using Qwen3 235B A22B free model
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.7,
)

db = SQLDatabase.from_uri("sqlite:///db.sqlite3")

# Define a custom prompt template optimized for chat mode
custom_prompt = PromptTemplate.from_template(
    """
You are a helpful shopping assistant. You provide direct, concise answers about products and categories in our store. You don't need to explain your reasoning or show your work unless specifically asked.

Use the following format:
Question: "Question here"
SQLQuery: "SQL Query to run"
SQLResult: "Result of the SQLQuery"
Answer: "Final answer here"

Only use the following tables:
{table_info}

If the user asks about a product, first consider if they might be referring to a category with the same name. If a product name is ambiguous (e.g., 'mouse' could be a product or a category), try to search for it as a category first, then as a product if no category is found. If the user asks for the price of a product, make sure to query the `selling_price` column.

If the user asks for information that is not related to products, categories, or general greetings, or if they ask for sensitive information such as user details, passwords, or other private data, respond with: "Hey, I am only here to help you with your shopping."

Question: {input}
"""
)

db_chain = SQLDatabaseChain.from_llm(
    llm, db, prompt=custom_prompt, verbose=True, return_sql=True
)


@login_required
def chat(request):
    if request.method == "POST":
        user_input = request.POST.get("user_input")

        # Save user message to history
        ChatHistory.objects.create(
            user=request.user, message=user_input, is_user_message=True
        )

        # Pre-process user input for greetings and sensitive questions
        user_input_lower = user_input.lower()
        user_info_keywords = [
            "user",
            "profile",
            "account",
            "password",
            "email",
            "address",
            "phone",
            "full_name",
            "zip_code",
            "city",
            "country",
        ]

        if any(
            greeting in user_input_lower
            for greeting in ["hello", "hi", "hey", "how are you"]
        ):
            response = "Hello! How can I assist you with your shopping today?"
        elif any(
            keyword in user_input_lower for keyword in user_info_keywords
        ):
            response = "For privacy reasons, I cannot answer questions about user information."
        else:
            # Get the response from the LLM using the db_chain
            try:
                response = db_chain.run(user_input)
            except Exception as e:
                # Log the error for debugging
                logger.error(f"Error in chatbot: {str(e)}")
                
                # Handle specific OpenRouter API errors
                if "rate limit" in str(e).lower():
                    response = "I'm experiencing high demand right now. Please wait a moment and try again."
                elif "unauthorized" in str(e).lower() or "api key" in str(e).lower():
                    response = "I'm having trouble connecting to my brain. Please contact support."
                else:
                    response = "I encountered an issue processing your request. Please try rephrasing or ask another question."

        # Save bot response to history
        ChatHistory.objects.create(
            user=request.user, message=response, is_user_message=False
        )

        return JsonResponse({"response": response})

    chat_history = ChatHistory.objects.filter(user=request.user).order_by(
        "timestamp"
    )
    return render(request, "chatbot/chat.html", {"chat_history": chat_history})
