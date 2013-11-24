from django.db import models

class Testimonial(models.Model):
	source = models.CharField(max_length=255, help_text='The person or organization making the statement.')
	statement = models.TextField(help_text='No HTML is allowed.')
	source_link = models.URLField(help_text='The website of the person or organization making the statement.', blank=True)
	is_featured = models.BooleanField(default=False, help_text='Check this box to add this testimonial to the homepage.')
	
	class Meta:
		verbose_name = 'testimonial'
		verbose_name_plural = 'testimonials'
	
	def __unicode__(self):
		return self.source