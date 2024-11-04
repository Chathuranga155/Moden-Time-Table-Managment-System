from django import template

register = template.Library()

@register.filter
def add_prefix(value, prefix):
    return f"{prefix}{value}"



from django import template

register = template.Library()

@register.filter
def add_class(field, css_class):
    return field.as_widget(attrs={'class': css_class})

@register.filter
def add_placeholder(field, placeholder):
    return field.as_widget(attrs={'placeholder': placeholder})
