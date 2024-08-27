from django.contrib import admin
from .models import Shop, ProductImage, ProductVersion
from django.utils.html import format_html

# Inline для отображения изображений в ProductVersion
class ProductImageInline(admin.TabularInline):
    model = ProductVersion.images.through
    extra = 1

class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_new', 'is_published', 'get_main_version_image']
    list_filter = ['is_published']
    list_editable = ['is_new', 'is_published']
    search_fields = ['name']
    readonly_fields = ['created','update']
    fieldsets = [
        ("Basic Information", {'fields': ('name', 'price', 'endirim')}),
        ('Additional Information', {'fields': ('description', 'RewardPoints', 'category', 'manufacturer', 'Availability', 'star', 'is_new', 'is_published', 'main_version')}),
        ('Əlave punktlar', {'fields': ('created','update')}),
    ]

    def get_main_version_image(self, obj):
        if obj.main_version and obj.main_version.cover_image:
            img = '<img src="{url}" width="100px" height="100px" style="object-fit: cover;"/>'.format(url=obj.main_version.cover_image.url)
            return format_html(img)
        return format_html('<p style="color: red;">No image</p>')

    get_main_version_image.short_description = 'Main Version Image'

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_image']
    search_fields = ['title']
    fieldsets = [
        ("Image", {"fields": ('image',)}),
        ("Image Title", {"fields": ('title',)})
    ]

    def get_image(self, obj):
        if obj.image:
            img = '<img src="{url}" width="200px" height="100px" style="object-fit: cover;"/>'.format(url=obj.image.url)
            return format_html(img)
        return format_html('<p style="color: red;">No image</p>')

    get_image.short_description = 'Image'

class ProductVersionAdmin(admin.ModelAdmin):
    list_display = ['product', 'color', 'get_hover_image']
    search_fields = ['color']
    inlines = [ProductImageInline]

    def get_hover_image(self, obj):
        if obj.imageHover:
            img = '<img src="{url}" width="100px" height="100px" style="object-fit: cover;"/>'.format(url=obj.imageHover.url)
            return format_html(img)
        return format_html('<p style="color: red;">No image</p>')

    get_hover_image.short_description = 'Hover Image'

admin.site.register(Shop, ShopAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductVersion, ProductVersionAdmin)
