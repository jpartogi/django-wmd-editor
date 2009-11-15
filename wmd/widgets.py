from django import forms
from django.conf import settings
from django.forms.util import flatatt
from django.utils.html import escape
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.contrib.admin import widgets as admin_widgets

from wmd.settings import WMD_SHOW_PREVIEW, WMD_ADMIN_SHOW_PREVIEW

class MarkDownInput(forms.Textarea):
    class Media:
        js = ('/wmd-settings/js/', settings.MEDIA_URL + "/wmd/wmd.js")
        css = dict(screen = ['/wmd/css/'])

    def render(self, name, value, attrs=None):
        if value is None: value = ''

        final_attrs = self.build_attrs(attrs, name=name)

        html = [u'<textarea%s>%s</textarea>' % (flatatt(final_attrs),
                force_unicode(escape(value)))]

        if WMD_SHOW_PREVIEW:
            #TODO: Maybe we can generate an id here?
            html.append(u'<div class="wmd-preview"></div>')

        return mark_safe(u'\n'.join(html))

class AdminMarkDownInput(admin_widgets.AdminTextareaWidget, MarkDownInput):
    # The admin input has its own attribute to show the preview
    def render(self, name, value, attrs=None):
        if value is None: value = ''

        final_attrs = self.build_attrs(attrs, name=name)

        html = [u'<textarea%s>%s</textarea>' % (flatatt(final_attrs),
                force_unicode(escape(value)))]

        if WMD_ADMIN_SHOW_PREVIEW:
            html.append(u'<div class="wmd-preview"></div>')

        return mark_safe(u'\n'.join(html))