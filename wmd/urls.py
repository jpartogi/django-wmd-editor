# $Id: urls.py 858ffff7c9a1 2009/08/16 12:42:35 jpartogi $

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^wmd/js/$', 'wmd.views.wmd_js', name='wmd-js'),
    url(r'^wmd-settings/js/$', 'wmd.views.wmd_settings_js', name='wmd-settings-js'),
)