from django.contrib import admin

from orders.products.models import Town, Product


@admin.register(Town)
class TownAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'quantity', 'multiple_amount', 'is_active', 'updated_on')
    list_editable = ('price', 'quantity')
