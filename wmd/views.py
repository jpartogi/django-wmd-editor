# $Id: views.py 858ffff7c9a1 2009/08/16 12:42:35 jpartogi $

from django.http import HttpResponse
from django.template import loader, RequestContext

from wmd.settings import *

def wmd_js(request):
    template_files = (
        'wmd/wmd.js',
    )
    template = loader.select_template(template_files)

    context = RequestContext(request)

    return HttpResponse(template.render(context),
            content_type="application/x-javascript")

def wmd_settings_js(request):
    template_files = (
        'wmd-settings.js',
    )

    template = loader.select_template(template_files)

    settings = {
        'WMD_OUTPUT' : WMD_OUTPUT,
    }

    context = RequestContext(request, settings )

    return HttpResponse(template.render(context),
            content_type="application/x-javascript")