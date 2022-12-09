from django import template

register = template.Library()

@register.filter()
def censor(value):
    for word in value.split():
        forbidden_words = ('тупой', 'глупый', 'глупа', 'идиотина', 'толстого')
        if word.lower() in forbidden_words:
            check = f'{word[0]}{word[1:-1].replace(word[1:-1], len(word[1:-1]) * "*")}{word[-1]}'
            value = value.replace(word, check)
    return value



