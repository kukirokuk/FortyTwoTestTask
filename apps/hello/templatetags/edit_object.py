from django import template
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.contenttypes.models import ContentType


register = template.Library()


@register.simple_tag(takes_context=True)
def edit_link(context, object):
    context_var = context['info']
    if not isinstance(context_var, models.Model):
        return 'Just model should be passed to the templatag'
    item = ContentType.objects.get_for_model(object.__class__)
    return reverse('admin:%s_%s_change'
                   % (item.app_label, item.name), args=(object.id,))
