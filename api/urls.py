from django.conf.urls import patterns, url

urlpatterns = patterns('',
  url('skills/$', 'api.views.skills'),
)
