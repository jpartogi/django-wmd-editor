from django.core.cache import cache
from django.http import HttpResponse
from django.template import loader, RequestContext

from wmd import settings as wmd_settings
from wmd.models import *

def wmd_css(request):
    template_files = (
        'wmd.css',
    )
    template = loader.select_template(template_files)

    context = RequestContext(request)
    
    return HttpResponse(template.render(context), content_type="text/css")