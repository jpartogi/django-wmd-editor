# $Id: widgets.py 6d33f21c6e8a 2009/08/15 06:33:15 jpartogi $

from util import flatatt

from django.forms.widgets import Textarea
from django.utils.html import conditional_escape
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.contrib.admin import widgets as admin_widgets

class MarkDownInput(Textarea):
    def render(self, name, value, attrs=None):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        return mark_safe(u'<textarea%s>%s</textarea>' % (flatatt(final_attrs),
                conditional_escape(force_unicode(value))))

class AdminMarkDownInput(admin_widgets.AdminTextareaWidget, MarkDownInput):
    pass
