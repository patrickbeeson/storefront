from django.contrib import admin

from storefront.apparel.models import Product, Color, Feature, Technology, Size, Season, PersonType

class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'is_available')
	list_filter = ('is_available', 'colors', 'seasons', 'categories')
	prepopulated_fields = {"slug": ("name",)}
	raw_id_fields = ("photoset", 'lead_photo')
	
	fieldsets = (
		(None, {
			'fields': ('name', 'slug', 'description', 'lead_photo', 'photoset', 'template', 'categories', 'is_available')
		}),
		('Product details', {
			'classes': ('collapse',),
			'fields': ('material', 'technology', 'colors', 'sizing', 'seasons')
		}),
	)

admin.site.register(Product, ProductAdmin)
admin.site.register(Color)
admin.site.register(Feature)
admin.site.register(Technology)
admin.site.register(Season)
admin.site.register(Size)
admin.site.register(PersonType)