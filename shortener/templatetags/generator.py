from django import template


register = template.Library()


@register.filter
def gen(val):
    ''' Generates Serial row no '''
    return next(val)
