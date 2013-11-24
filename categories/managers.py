from django.db import models


class CategorySlugManager(models.Manager):
    def __init__(self, category_field="primary_category", slug_field="slug",
            *args, **kwargs):
        super(CategorySlugManager, self).__init__(*args, **kwargs)
        self.category_field = category_field
        self.slug_field = slug_field

    def get_by_slug(self, slug):
        if slug[-1] == "/":
            slug = slug[0:-1]
        if slug[0] == "/":
            slug = slug[1:]
        category_slug, content_slug = slug.rsplit("/", 1)
        category_slug += "/"
        kwargs = {
                "%s__full_slug" % self.category_field: category_slug,
                self.slug_field: content_slug,
        }
        qs = self.model.objects.filter(**kwargs)
        if hasattr(qs, "select_subclasses"):
            qs = qs.select_subclasses()
        try:
            return qs[0]
        except IndexError:
            raise self.model.DoesNotExist