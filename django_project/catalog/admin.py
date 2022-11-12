from django.contrib import admin
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail
from catalog.models import Item, Tag, Category, Gallery, Preview

admin.site.register(Tag)
admin.site.register(Category)


class PhotoGaleryInline(admin.TabularInline):
    model = Preview
    name = 'fk_item'


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'is_published',
                    'image_tmb',)
    list_editable = ('is_published',)
    list_display_links = ('name',)
    filter_horizontal = ('tags',)

    inlines = [PhotoGaleryInline]


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('item', 'image', 'image_tmb',)
    list_editable = ('image',)
