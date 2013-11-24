from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from storefront.media.models import Photo, PhotoSet

class PhotoSetAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	list_display = ('title', 'is_active')
	list_filter = ('is_active', 'categories', 'created')
	
	fieldsets = (
		(None, {
			'fields': ('title', 'slug', 'description', 'cover_photo', 'photos', 'categories', 'is_active')
		}),
	)

class PhotoAdmin(AdminImageMixin, admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	list_display = ('title', 'is_active')
	list_filter = ('is_active', 'categories', 'uploaded')
	
	fieldsets = (
		(None, {
			'fields': ('title', 'slug', 'description', 'taken_by', 'photo', 'categories', 'is_active')
		}),
	)
	
admin.site.register(Photo, PhotoAdmin)
admin.site.register(PhotoSet, PhotoSetAdmin)