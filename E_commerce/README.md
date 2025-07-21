# E-commerce Project

This is a Django-based e-commerce project that provides a platform for users to browse products, manage their carts, place orders, and interact with a chatbot.

## Features

The project is structured into several Django applications, each handling specific functionalities:

*   **`base`**: Manages core e-commerce functionalities such as products, categories, and product listings.
*   **`user`**: Handles user authentication, registration, login, logout, and user profile management.
*   **`order`**: Manages the shopping cart, checkout process, and user order history.
*   **`payment`**: Integrates payment processing functionalities for handling transactions.
*   **`chatbot`**: Provides an interactive chatbot for customer support, product inquiries, or other assistance.

## Technologies Used

*   **Django**: Web framework for rapid development.
*   **asgiref**: ASGI specification for Python web servers.
*   **sqlparse**: Non-validating SQL parser.
*   **python-dotenv**: Reads key-value pairs from a `.env` file and sets them as environment variables.
*   **langchain**, **langchain-community**, **langchain-experimental**: Libraries for developing applications with language models, likely used for the chatbot functionality.

## Setup

To set up and run this project locally, follow these steps:

1.  **Clone the repository**:

    ```bash
    git clone <repository_url>
    cd E_commerce
    ```

2.  **Create a virtual environment** (recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations**:

    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser** (for admin access):

    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server**:

    ```bash
    python manage.py runserver
    ```

    The application will be accessible at `http://127.0.0.1:8000/` (or the port specified in your environment variables).