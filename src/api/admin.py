from django.contrib import admin

from . import models


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        # 'id',
        'name',
        'price',
        'currency',
    )
    search_fields = ['name', 'description']
    list_editable = ['price']
