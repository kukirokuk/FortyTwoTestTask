from django import forms
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


class ButtonWidget(forms.Widget):
    template_name = 'cancel_button_widget.html'

    def render(self, name, value, attrs={'class': 'cancel'}):
        context = {'url': '/'}
        return mark_safe(render_to_string(self.template_name, context))
