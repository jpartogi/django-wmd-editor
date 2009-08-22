# $Id: widgets.py cbfb8c2202d7 2009/08/22 07:52:56 jpartogi $

from django import forms
from django.forms.util import flatatt
from django.utils.html import escape
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.contrib.admin import widgets as admin_widgets
from django.core.urlresolvers import reverse

class MarkDownInput(forms.Textarea):
    def render(self, name, value, attrs=None):
        if value is None: value = ''

        final_attrs = self.build_attrs(attrs, name=name)

        html = [u'<textarea%s>%s</textarea>' % (flatatt(final_attrs),
                force_unicode(escape(value)))]

        html.append(u'<div class="wmd-preview"></div>')
        return mark_safe(u'\n'.join(html))
    
    def _get_media(self):
        # wmd settings must come first
        js = [reverse('wmd-settings-js'), reverse('wmd-js')]

        css = dict(screen = [reverse('wmd-css')])
      
        return forms.Media(js=js, css=css)
    
    media = property(_get_media)
    
class AdminMarkDownInput(admin_widgets.AdminTextareaWidget, MarkDownInput):
    pass
