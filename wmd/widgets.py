from django import forms
from django.conf import settings
from django.forms.util import flatatt
from django.utils.html import escape
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.contrib.admin import widgets as admin_widgets

from wmd import settings as wmd_settings

class MarkDownInput(forms.Textarea):
    class Media:
        js = ('/wmd-settings/js/', settings.MEDIA_URL + "/wmd/wmd.js")
        css = dict(screen = ['/wmd/css/'])

    def render(self, name, value, attrs=None):
        if value is None: value = ''

        final_attrs = self.build_attrs(attrs, name=name)

        html = [u'<textarea%s>%s</textarea>' % (flatatt(final_attrs),
                force_unicode(escape(value)))]

        if wmd_settings.WMD_SHOW_PREVIEW:
            #TODO: Maybe we can generate ids here if there are more than one editor?
            html.append(u'<div class="wmd-preview"></div>')

        return mark_safe(u'\n'.join(html))

class AdminMarkDownInput(admin_widgets.AdminTextareaWidget, MarkDownInput):
    # The admin input has its own attribute to show the preview or not
    def render(self, name, value, attrs=None):
        if value is None: value = ''

        final_attrs = self.build_attrs(attrs, name=name)

        html = [u'<textarea%s>%s</textarea>' % (flatatt(final_attrs),
                force_unicode(escape(value)))]

        if wmd_settings.WMD_ADMIN_SHOW_PREVIEW:
            html.append(u'<div class="wmd-preview"></div>')

        return mark_safe(u'\n'.join(html))