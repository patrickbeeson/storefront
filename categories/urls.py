from django.conf.urls.defaults import patterns, include, url

from storefront.categories.models import Category
from storefront.categories.views import SimpleCategoryView

urlpatterns = patterns('',
	url(r'^(?P<full_slug>[-\w/]+)', SimpleCategoryView.as_view(), name='category_view'),
)