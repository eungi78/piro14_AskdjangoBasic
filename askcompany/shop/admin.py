from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'short_desc', 'price', 'is_published']
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ['is_published']
    pass

    def short_desc(self, item):  # 원하는 이름으로 함수 하나를 만들고, 인자로 등록한 모델의 객체가 자동으로 넘어옴
        return item.desc[:20]
