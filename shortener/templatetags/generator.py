from django import template


register = template.Library()


@register.filter
def gen(val):
    ''' Generates Serial row no '''
    return next(val)


@register.filter
def genshortlen(val):
    ''' short long-link characters for simple view '''
    if val[:8] == 'https://':
        return f'{val[8:20]}...'
    elif val[:7] == 'http://':
        return f'{val[7:19]}...'
    else:
        return f'{val[:12]}...'
