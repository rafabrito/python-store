from django import template

register = template.Library()

@register.filter(name='coverter_para_dict')
def coverter_para_dict(dado):
    
    return dado.__dict__