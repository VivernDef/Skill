from django import template
from django.core.paginator import Paginator

register = template.Library()


@register.filter()
def censor(value):
    for word in value.split():
        forbidden_words = ('тупой', 'глупый', 'глупа', 'идиотина', 'толстого')
        if word.lower() in forbidden_words:
            check = f'{word[0]}{word[1:-1].replace(word[1:-1], len(word[1:-1]) * "*")}{word[-1]}'
            value = value.replace(word, check)
    return value


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
   d = context['request'].GET.copy()
   for k, v in kwargs.items():
       d[k] = v
   return d.urlencode()


@register.simple_tag()
def get_elided_page_range(p, number, on_each_side=2, on_ends=1):
    paginator = Paginator(p.object_list, p.per_page)
    return paginator.get_elided_page_range(number=number,
                                           on_each_side=on_each_side,
                                           on_ends=on_ends)


