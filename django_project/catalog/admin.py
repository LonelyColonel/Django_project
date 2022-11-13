from django.contrib import admin
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail
from catalog.models import Item, Tag, Category, Gallery

admin.site.register(Tag)
admin.site.register(Category)


class PhotoGaleryInline(admin.TabularInline):
    model = Gallery
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
    list_display = ('item', 'image', 'image_tmb')
    list_editable = ('image',)

    def get_image(self, obj):
        return get_thumbnail(obj.image, '300x300', crop='center', quality=51)

    def image_tmb(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{self.get_image(obj).url}">')
        return 'нет изображения'

    image_tmb.short_descriptions = 'картинка'
    image_tmb.allow_tags = True
