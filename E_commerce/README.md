# E-commerce Project

A Django-based e-commerce platform with integrated AI chatbot functionality.

## Features
- Product catalog with categories
- User authentication and profiles
- Shopping cart functionality
- Order management
- Payment integration
- AI-powered chatbot (using Qwen3 235B A22B via OpenRouter)

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables:
   ```bash
   export OPENROUTER_API_KEY="your-openrouter-api-key"
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Chatbot

The chatbot uses the Qwen3 235B A22B (free tier) model via OpenRouter API to assist users with:
- Product information
- Category details
- General shopping queries

Privacy Notice: The chatbot cannot access sensitive user information such as passwords, addresses, or payment details.

## Environment Variables

- `OPENROUTER_API_KEY`: Your OpenRouter API key (required for chatbot)