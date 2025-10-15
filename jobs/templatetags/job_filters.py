from django import template

register = template.Library()

@register.filter
def split_lines(value):
    """Split text by line breaks and return as list"""
    if not value:
        return []
    return [line.strip() for line in value.split('\n') if line.strip()]
