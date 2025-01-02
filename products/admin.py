from django.contrib import admin

from django.contrib import admin
from .models import Material, Category


class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        'video_name',
        'pdf_name',
        'category',
    )

    ordering = ('material_title',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'difficulty_level',
        'credits',
        'number_of_lectures',
        'est_time',
        'short_description',
        'test',
    )

    ordering = ('friendly_name',)


admin.site.register(Material, MaterialAdmin)
admin.site.register(Category, CategoryAdmin)