from django import template

register = template.Library()



@register.inclusion_tag('block/navbar.html')
def show_navbar(section):
    return {'section': section}

@register.inclusion_tag('block/footer.html')
def show_footer(section):
    return {'section': section}


