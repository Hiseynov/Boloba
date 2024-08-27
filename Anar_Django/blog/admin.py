from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from django.utils.html import format_html
from .models import *
# Register your models here.
class BlogAdmin(TranslationAdmin,admin.ModelAdmin):
    list_display = ['title','is_publised','get_image'] # ilk gorusde hansilar gorunsun
    list_filter = ['is_publised'] #admin pagde filtirasiya aparmag
    list_editable = ['is_publised']  #admin pagde detalina girmeden deyisile bilmek
    search_fields =['title'] # neye gore search edilsin
    readonly_fields = ['created','update']
    fieldsets = [
        ("Əsas punktlar", {'fields': ('title','image')}),
        ('Əlave punktlar', {'fields': ('desgription','is_publised','created','update')}),
    ]
   
    def get_image(self,obj):
        if obj.image:
            img = '<img src= "{url}"  width ="100px"  height ="100px" object-fit ="cover"/>'.format(url = obj.image.url)
            return format_html(img)
        return format_html('<p style =color="red"">No image </p>')

admin.site.register(Blogs,BlogAdmin)
admin.site.register(Comment) 

