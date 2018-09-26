from django.contrib import admin
from app.models import GetingUsersEmails
# Register your models here.


class GetingUserEmailsAdmin(admin.ModelAdmin):
    readonly_fields = ('registerd_at',)


admin.site.register(GetingUsersEmails, GetingUserEmailsAdmin)
