# $Id: settings.py bf90bf6ed969 2009/08/16 13:58:10 jpartogi $

from django.conf import settings

WMD_OUTPUT = getattr(settings, 'WMD_OUTPUT', "Markdown")
WMD_LINE_LENGTH = getattr(settings, 'WMD_LINE_LENGTH', 40)
WMD_BUTTONS = getattr(settings, 'WMD_BUTTONS', "bold italic | link blockquote code image | ol ul heading hr")