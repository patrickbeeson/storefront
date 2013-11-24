from django.db import models
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey

class CategoryManager(models.Manager):
	def get(self, **kwargs):
		defaults = {}
		defaults.update(kwargs)
		if 'full_slug' in defaults:
			if defaults['full_slug'] and defaults['full_slug'][-1] != "/":
				defaults['full_slug'] += "/"
		return super(CategoryManager, self).get(**defaults)

class Category(MPTTModel):
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True, help_text='A brief description of the category. No HTML allowed.')
	slug = models.SlugField(help_text='Prepopulates from title field.')
	full_slug = models.CharField(max_length=255, blank=True)
	template_name = models.CharField(max_length=70, blank=True, help_text="Example: 'categories/category_parent.html'. If this isn't provided, the system will use 'categories/category_detail.html'.")

	parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

	objects = CategoryManager()

	class Meta:
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def save(self, *args, **kwargs):
		orig_full_slug = self.full_slug
		if self.parent:
			self.full_slug = "%s%s/" % (self.parent.full_slug, self.slug)
		else:
			self.full_slug = "%s/" % self.slug
		obj = super(Category, self).save(*args, **kwargs)
		if orig_full_slug != self.full_slug:
			for child in self.get_children():
				child.save()
		return obj

	def __unicode__(self):
		return "%s (%s)" % (self.title, self.full_slug)

	def get_absolute_url(self):
		return '/categories/%s' % (self.full_slug)