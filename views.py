from django.views.generic import TemplateView

from storefront.testimonials.models import Testimonial

class RobotsView(TemplateView):
	
	template_name = "robots.txt"
	
	def render_to_response(self, context, **kwargs):
		return super(RobotsView, self).render_to_response(context, content_type='text/plain', **kwargs)
		
class HomePageView(TemplateView):
	
	template_name = "home.html"

	def get_context_data(self, **kwargs):
		context = super(HomePageView, self).get_context_data(**kwargs)
		context['testimonial_list'] = Testimonial.objects.all().filter(is_featured=True)
		return context