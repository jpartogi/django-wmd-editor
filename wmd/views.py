from django.core.cache import cache
from django.http import HttpResponse
from django.template import loader, RequestContext

from wmd import settings as wmd_settings
from wmd.models import *

def wmd_settings_js(request):
    template_files = (
        'wmd-settings.js',
    )

    template = loader.select_template(template_files)

    configs = cache.get('configs')
    
    if configs == None:
        configs = Config.objects.all()
        cache.set('configs', configs)
    
    WMD_OUTPUT = configs.get(key = 'WMD_OUTPUT').value or wmd_settings.WMD_OUTPUT
    WMD_LINE_LENGTH = configs.get(key = 'WMD_LINE_LENGTH').value or wmd_settings.WMD_LINE_LENGTH
    WMD_BUTTONS = configs.get(key = 'WMD_BUTTONS').value or wmd_settings.WMD_BUTTONS

    settings = {
        'WMD_OUTPUT' : WMD_OUTPUT,
        'WMD_LINE_LENGTH': WMD_LINE_LENGTH,
        'WMD_BUTTONS' : WMD_BUTTONS,
    }

    context = RequestContext(request, settings )
    return HttpResponse(template.render(context),
            content_type="application/x-javascript")

def wmd_css(request):
    template_files = (
        'wmd.css',
    )
    template = loader.select_template(template_files)

    context = RequestContext(request)
    
    return HttpResponse(template.render(context), content_type="text/css")