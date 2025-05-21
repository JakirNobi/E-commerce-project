from django import template
from base.models import Category

register = template.Library()

@register.filter

def category(user):
        cat = Category.objects.all()
        return cat