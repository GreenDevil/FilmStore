from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'films_store.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^films/all/$', 'films.views.films'),
    url(r'^films/get/(?P<films_id>\d+)/$', 'films.views.film'),
    url(r'^films/addcomment/(?P<films_id>\d+)/$', 'films.views.addcomment'),
    url(r'^films/addorder/1/$', 'films.views.addorder'),
    url(r'^$', 'films.views.films'),

)
