
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^wmd/css/$', 'wmd.views.wmd_css', name='wmd-css'),
)