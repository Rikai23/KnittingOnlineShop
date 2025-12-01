from django.contrib import admin

from goods.models import Categories, Products, ProductImage

admin.site.register(Categories)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]  # вот здесь привязываем инлайн к продукту