from django import template
from django.core.urlresolvers import reverse
from django.db import models


register = template.Library()


def link(obj):
    return reverse('admin:%s_%s_change'
                   % (obj._meta.app_label, obj._meta.module_name),
                   args=[obj.id])


class AdminEditNode(template.Node):
    def __init__(self, object):
        self.object = template.Variable(object)

    def render(self, context):
        resolved = self.object.resolve(context)
        if not isinstance(resolved, models.Model):
            return 'Just model should be passed to the templatag'
        return link(resolved)


def edit_link(parser, token):
    try:
        # split content
        tag_name, info = token.split_contents()

    except ValueError:
        raise template.TemplateSyntaxError(
            '%r tag requires one model argument' % token.contents.split()[0])
    return AdminEditNode(info)

register.tag('edit_link', edit_link)
