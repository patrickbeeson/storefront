from django.contrib import admin

from storefront.testimonials.models import Testimonial

class TestimonialAdmin(admin.ModelAdmin):
	list_display = ('source', 'is_featured')
	list_filter = ['is_featured']

admin.site.register(Testimonial, TestimonialAdmin)