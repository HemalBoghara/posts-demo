from masonry.models import Categories, SubCategories

from django import template
register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def menu(context):
    resultCategories = Categories.objects.filter(parent__isnull=True).values()

    resultSubCategories = SubCategories.objects.filter(
        parent__isnull=False).values()
    # print(resultSubCategories)
    return {
        'resultCategories': resultCategories,
        'resultSubCategories': resultSubCategories,
    }
