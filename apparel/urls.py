from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, DetailView

from storefront.apparel.models import Product

urlpatterns = patterns('',
    url(r'^(?P<slug>[-\w]+)/$', DetailView.as_view(
    	context_object_name = "product",
		template_name = "apparel/product_detail.html",
    	model = Product,
    )),
	#url(r'^$', ListView.as_view(
	#	model = Product,
	#	context_object_name = "product_list",
	#	paginate_by = 15,
	#)),
)