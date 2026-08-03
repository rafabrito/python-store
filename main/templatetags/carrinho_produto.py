from django import template

register = template.Library()

@register.filter(name='total_produto')
def total_produto(carrinho):
    total_produto = 0
    if carrinho:
        for chave in carrinho:
            total_produto += carrinho[chave]

    total_produto = '' if total_produto == 0 else total_produto
    return total_produto