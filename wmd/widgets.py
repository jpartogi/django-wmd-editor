# $Id: widgets.py 5f79ec26972e 2009/08/15 06:22:28 jpartogi $

from django.forms.widgets import Textarea
from django.utils.html import conditional_escape
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

class MarkDownInput(Textarea):
    def render(self, name, value, attrs=None):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        return mark_safe(u'<textarea%s>%s</textarea>' % (flatatt(final_attrs),
                conditional_escape(force_unicode(value))))