from django import template
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType


register = template.Library()


@register.simple_tag
def edit_link(object):
    item = ContentType.objects.get_for_model(object.__class__)
    return reverse('admin:%s_%s_change'
                   % (item.app_label, item.name), args=(object.id,))
