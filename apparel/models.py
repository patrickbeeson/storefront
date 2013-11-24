from django.db import models

from storefront.media.models import PhotoSet, Photo
from storefront.categories.models import Category
from storefront.categories.managers import CategorySlugManager

class Color(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True, help_text='A brief description of the color. No HTML allowed.')

	class Meta:
		verbose_name = 'color'
		verbose_name_plural = 'colors'

	def __unicode__(self):
		return self.name

class Feature(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True, help_text='A brief description of the feature. No HTML allowed.')

	class Meta:
		verbose_name = 'feature'
		verbose_name_plural = 'features'

	def __unicode__(self):
		return self.name

class Technology(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True, help_text='A brief description of the technology. No HTML allowed.')

	class Meta:
		verbose_name = 'technology'
		verbose_name_plural = 'technology'

	def __unicode__(self):
		return self.name

class PersonType(models.Model):
	type = models.CharField(max_length=255)

	class Meta:
		verbose_name = 'person type'
		verbose_name_plural = 'person types'
	
	def __unicode__(self):
		return self.type

class Size(models.Model):
	name = models.CharField(max_length=255)
	person_type = models.ManyToManyField(PersonType)
	description = models.TextField(blank=True, help_text='A brief description of the size. No HTML allowed.')

	class Meta:
		verbose_name = 'size'
		verbose_name_plural = 'sizes'

	def __unicode__(self):
		return self.name

class Season(models.Model):
	name = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.name

class ProductManager(models.Manager):
    
    def available(self):
        return super(ProductManager, self).get_query_set().filter(is_available=True)

class Product(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField(help_text='Prepopulates from name field.')
	description = models.TextField(blank=True, help_text='A brief description of the product. No HTML allowed.')
	material = models.TextField(blank=True, help_text='A brief description of the fabric or material for the product. No HTML allowed.')
	colors = models.ManyToManyField(Color, help_text='The colors available for this product.', blank=True)
	features = models.ManyToManyField(Feature, help_text='The features incorporated in this product.', blank=True)
	technology = models.ManyToManyField(Technology, help_text='The technology incorporated in this product.', blank=True)
	sizing = models.ManyToManyField(Size)
	categories = models.ManyToManyField(Category)
	with_category = CategorySlugManager(category_field="categories")
	seasons = models.ManyToManyField(Season)
	photoset = models.ForeignKey(PhotoSet, null=True, blank=True, help_text='Use this if you have multiple photos for a product.')
	lead_photo = models.ForeignKey(Photo, null=True, blank=True, help_text='Use this if want one lead photo for a product. Use the photoset field for multiple photos.')
	is_available = models.BooleanField(default=True, help_text='Uncheck this box if the product is no longer available.')
	template = models.FileField(upload_to='product_templates', blank=True, help_text='If the product has a downloadable template, please upload it here.')
	
	objects = ProductManager()

	class Meta:
		verbose_name = 'product'
		verbose_name_plural = 'products'

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return '/apparel/%s/' % (self.slug)

	@property
	def related_product_set(self):
		category_id_list = self.categories.values_list("id", flat=True)
		return Product.objects.filter(categories__id__in=category_id_list).exclude(id=self.id).distinct()