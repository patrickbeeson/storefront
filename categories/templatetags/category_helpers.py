from storefront.categories.models import Category
from django.utils.safestring import mark_safe as _
from django import template as djtemplate
from django.template.loader import render_to_string
from django.template.defaulttags import token_kwargs

register = djtemplate.Library()


class CategoryMenuNode(djtemplate.Node):
    def __init__(self,
            template=None,
            category_view=None,
            categories=None):
        self.template = template
        self.category_view = category_view
        self.categories = categories

    def render(self, context):
        if self.template is None:
            template = 'categories/categories_menu.html'
        else:
            template = self.template.resolve(context)

        if self.categories is None:
            categories = Category.objects.all().order_by('tree_id')
        else:
            categories = self.categories.resolve(context)

        dictionary = {'categories': categories,
                      'category_view': self.category_view,
                     }
        return render_to_string(template, dictionary=dictionary)


@register.tag(name='category_menu')
def do_category_menu(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        args = token.split_contents()[1:]
        kwargs = token_kwargs(args, parser)
        if len(args) > 0:
            raise ValueError
    except ValueError:
        raise djtemplate.TemplateSyntaxError(
                "%r tag accepts only keyword arguments" \
                % token.contents.split()[0])
    return CategoryMenuNode(**kwargs)
