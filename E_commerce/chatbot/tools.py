from langchain.tools import tool
from base.models import Product, Category
from pydantic import BaseModel, Field

class GetProductDetailsInput(BaseModel):
    product_name: str = Field(description="The name of the product to get details for.")
    category_name: str | None = Field(None, description="Optional: The name of the category the product belongs to.")

@tool(args_schema=GetProductDetailsInput)
def get_product_details(product_name: str, category_name: str = None):
    """Returns the details of a specific product. Can optionally filter by category name."""
    try:
        if category_name:
            product = Product.objects.get(name__iexact=product_name, category__name__iexact=category_name)
        else:
            product = Product.objects.get(name__iexact=product_name)
        
        status = "in stock" if product.is_stock else "out of stock"
        return f"Product: {product.name}, Description: {product.full_description}, Price: ${product.selling_price:.2f}, Status: {status}."
    except Product.DoesNotExist:
        if category_name:
            return f"Product '{product_name}' not found in category '{category_name}'."
        else:
            return f"Product '{product_name}' not found."

@tool
def get_all_products():
    """Returns a list of all products in the store."""
    products = Product.objects.all()
    if products:
        return "Available products: " + ", ".join([product.name for product in products]) + "."
    else:
        return "No products found in the store."

@tool
def get_products_in_category(category_name: str):
    """Returns a list of all products in a specific category."""
    products = Product.objects.filter(category__name__iexact=category_name)
    if products:
        return f"Products in {category_name} category: " + ", ".join([product.name for product in products]) + "."
    else:
        return f"No products found in the '{category_name}' category."

@tool
def get_all_categories():
    """Returns a list of all available product categories."""
    categories = Category.objects.all()
    if categories:
        return "Available categories: " + ", ".join([category.name for category in categories]) + "."
    else:
        return "No categories found."

