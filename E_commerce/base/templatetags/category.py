from django import template
from base.models import Category
from django.db.models import Count

register = template.Library()

# @register.inclusion_tag('base/includes/category_list.html')
# def show_categories():
#     categories = Category.objects.annotate(product_count=Count('category'))
#     return {'categories': categories}

@register.filter
def category(user):
    if user.is_authenticated:
        cat = Category.objects.all()
        return cat
