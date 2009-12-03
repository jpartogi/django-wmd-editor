from django import forms
from django.conf import settings
from django.core.urlresolvers import reverse
from django.forms.util import flatatt
from django.utils.html import escape
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.contrib.admin import widgets as admin_widgets
from django.core.urlresolvers import reverse

from wmd import settings as wmd_settings

class MarkDownInput(forms.Textarea):
    def render(self, name, value, attrs=None):
        if value is None: value = ''

        final_attrs = self.build_attrs(attrs, name=name)

        html = [u'<textarea%s>%s</textarea>' % (flatatt(final_attrs),
                force_unicode(escape(value)))]

        if wmd_settings.WMD_SHOW_PREVIEW:
            #TODO: Maybe we can generate ids here if there are more than one editor?
            html.append(u'<div class="wmd-preview"></div>')

        return mark_safe(u'\n'.join(html))

    def _media(self):
        return forms.Media(css= dict(screen = [reverse('wmd-css')]),
                           js=(reverse('wmd-settings-js'), settings.MEDIA_URL + "/wmd/wmd.js"))

    media = property(_media)

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