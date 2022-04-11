from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    if dictionary.get(key):
        return dictionary.get(key)
