from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'films_store.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^animation/', TemplateView.as_view(template_name='animation.html'), name='animation'),
    url(r'^about/', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^', include('films.urls')),
)
