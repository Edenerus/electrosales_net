from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "company_link")
    search_fields = ("username", "email", "first_name", "last_name")
    readonly_fields = ("last_login", "date_joined")

    def company_link(self, obj):
        if obj.company:
            link = reverse(
                'admin:network_provider_change',
                args=(obj.company.id,)
            )
            return mark_safe(
                u"<a href='{0}'>{1}</a>".format(link, obj.company)
            )
