from django.contrib import admin

from orders.products.models import Category


@admin.register(Category)
class CategoryAdin(admin.ModelAdmin):
    pass
