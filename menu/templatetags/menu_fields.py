from django import template
from django.shortcuts import get_object_or_404
from menu.models import Menu
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

register = template.Library()

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    print(context)
    menu = get_object_or_404(Menu, name=menu_name, parent=None)
    # print(menu)
    tag_context = {'menu_item': menu}
    requested_url = context['request'].path

    try:
        active_menu_item = Menu.objects.get(url=requested_url)
    except ObjectDoesNotExist:
        raise Http404("Given query not found....")
    else:
        opented_menu_items = active_menu_item.get_parent_id() + [active_menu_item.id]
        # print(opented_menu_items)
        tag_context['opented_menu_items'] = opented_menu_items

    return tag_context


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu_children(context, menu_item_id):
    # print(context)
    menu_item = get_object_or_404(Menu, pk=menu_item_id)
    tag_context = {'menu_item': menu_item}

    if 'opented_menu_items' in context:
        tag_context['opented_menu_items'] = context['opented_menu_items']

    return tag_context
