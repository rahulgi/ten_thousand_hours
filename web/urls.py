from django.conf.urls import patterns, url

urlpatterns = patterns('',
  url('^$', 'web.views.index'),
  url('^create_skill/$', 'web.views.create_skill'),
  url('^skills/(?P<pk>[0-9]+)/$', 'web.views.skill'),
  url('^skills/(?P<pk>[0-9]+)/add_time/$', 'web.views.add_skill_time'),
  url('^create_user/$', 'web.views.register', name='create-new-user'),
)
