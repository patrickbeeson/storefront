from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, DetailView
from django.views.generic.detail import SingleObjectTemplateResponseMixin, SingleObjectMixin
from django.utils.translation import ugettext as _
from django.contrib.syndication.views import Feed

from storefront.categories.models import Category

class SimpleCategoryView(TemplateView):

	def get_category(self):
		return Category.objects.get(full_slug=self.kwargs['full_slug'])

	def get_context_data(self, **kwargs):
		context = super(SimpleCategoryView, self).get_context_data(**kwargs)
		context["category"] = self.get_category()
		return context

	def get_template_names(self):
		if self.get_category().template_name:
			return [self.get_category().template_name]
		else:
			return ['categories/category_detail.html']

#class SectionFeed(Feed):
#	 def __init__(self, section_view, *args, **kwargs):
#		 self.section_view = section_view

#	 def get_object(self, request, full_slug):
#		 return Section.objects.get(full_slug=full_slug)

#	 def title(self, section):
#		 return section.title

#	 def link(self, section):
#		 return reverse(self.section_view,
#				 kwargs={'full_slug': section.full_slug})

#	 def description(self, section):
#		 return section.summary

#	 def items(self, section):
#		 return section.items
