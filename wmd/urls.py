# $Id: urls.py cbfb8c2202d7 2009/08/22 07:52:56 jpartogi $

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^wmd-settings/js/$', 'wmd.views.wmd_settings_js', name='wmd-settings-js'),
    url(r'^wmd/css/$', 'wmd.views.wmd_css', name='wmd-css'),
)