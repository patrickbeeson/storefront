from django.db import models
from sorl.thumbnail import ImageField

from storefront.categories.models import Category

class PhotoSetManager(models.Manager):
    
    def active(self):
        return super(PhotoSetManager, self).get_query_set().filter(is_active=True)

class PhotoSet(models.Model):
	is_active = models.BooleanField(help_text=("Tick to make this photoset live."), default=False)
	title = models.CharField(max_length=255)
	slug = models.SlugField(help_text='Prepopulates from title field.')
	description = models.TextField(blank=True, help_text='A brief description of the photoset. No HTML allowed.')
	cover_photo = models.ForeignKey('Photo', blank=True, null=True)
	photos = models.ManyToManyField('Photo', related_name='photo_sets')
	categories = models.ManyToManyField(Category, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	objects = PhotoSetManager()

	class Meta:
		db_table = 'media_photo_sets'
		verbose_name = 'photo set'
		verbose_name_plural = 'photo sets'

	def __unicode__(self):
		return '%s' % self.title

class PhotoManager(models.Manager):
    
    def active(self):
        return super(PhotoManager, self).get_query_set().filter(is_active=True)

class Photo(models.Model):
	is_active = models.BooleanField(help_text=("Tick to make this photo live."), default=False)
	title = models.CharField(max_length=255)
	slug = models.SlugField(help_text='Prepopulates from title field.')
	photo = models.ImageField(upload_to='photos')
	taken_by = models.CharField(max_length=100, blank=True)
	description = models.TextField(blank=True, help_text='A brief description of the photo. No HTML allowed.')
	categories = models.ManyToManyField(Category, blank=True, null=True)
	uploaded = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	objects = PhotoManager()

	class Meta:
		db_table = 'media_photos'
		verbose_name = 'photo'
		verbose_name_plural = 'photos'

	def __unicode__(self):
		return '%s' % self.title