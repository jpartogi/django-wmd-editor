from django.conf import settings

from wmd.models import *

try:
    WMD_OUTPUT = Config.objects.get(key='WMD_OUTPUT')
    print WMD_OUTPUT
except:
    WMD_OUTPUT = None
    #WMD_OUTPUT = getattr(settings, 'WMD_OUTPUT', "Markdown")


WMD_LINE_LENGTH = getattr(settings, 'WMD_LINE_LENGTH', 40)
WMD_BUTTONS = getattr(settings, 'WMD_BUTTONS', "bold italic | link blockquote code image | ol ul heading hr")

WMD_SHOW_PREVIEW = getattr(settings, 'WMD_SHOW_PREVIEW', False)
WMD_ADMIN_SHOW_PREVIEW = getattr(settings, 'WMD_ADMIN_SHOW_PREVIEW', False)