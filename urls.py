from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from storefront.views import RobotsView, HomePageView

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', HomePageView.as_view()),
	url(r'^categories/', include('storefront.categories.urls')),
	url(r'^apparel/', include('storefront.apparel.urls')),
	url(r'^contact/', include('contact_form.urls')),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^robots\.txt$', RobotsView.as_view()),
	url(r'', include('django.contrib.flatpages.urls')),
)