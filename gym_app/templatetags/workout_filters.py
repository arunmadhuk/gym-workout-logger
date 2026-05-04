from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiply the value by the argument"""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def multiply_three(value, arg1, arg2):
    """Multiply three values together"""
    try:
        return float(value) * float(arg1) * float(arg2)
    except (ValueError, TypeError):
        return 0