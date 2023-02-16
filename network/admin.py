from django.contrib import admin
from network.models import Item, Link


admin.site.register(Item)
admin.site.register(Link)

@admin.action(description='Изменение задолженности перед поставщиком')
def zero_debt(queryset):
    queryset.update(debt=0)
