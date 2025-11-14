from django import template

register = template.Library()


@register.filter
def num_range(value):
    return range(value)
