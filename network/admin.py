from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from network.models import Product, Provider


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'level', 'country', 'city', 'debt', 'provider_link', )
    list_per_page = 10
    list_filter = ('city', )
    fieldsets = [
        (None, {'fields': ['title', 'type', 'level', 'products', 'provider', 'debt', ]}),
        ('Contacts', {'fields': ['email', 'country', 'city', 'street', 'house']})
    ]
    readonly_fields = ('level', )
    actions = ['cancel_debt', ]

    def provider_link(self, obj):
        """Ссылка на поставщика"""
        if obj.provider:
            link = reverse('admin:network_provider_change', args=(obj.provider.id,))

            return mark_safe(u"<a href='{0}'>{1}</a>".format(link, obj.provider))

    @admin.action(description="Обнулить задолженность")
    def cancel_debt(self, request, queryset):
        """Обнуление задолженности перед поставщиком"""
        queryset.update(debt=0)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'model', 'date_release', )
    list_filter = ('title', )
    search_fields = ('title', 'model', )
