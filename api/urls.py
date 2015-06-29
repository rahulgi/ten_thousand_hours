from django.conf.urls import patterns, url

urlpatterns = patterns('',
  url('skills/$', 'api.views.skills'),
  url('skill/(?P<pk>[0-9]+)/times/$', 'api.views.skill_times'),
)
