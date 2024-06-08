from django.contrib import admin
from .models import JobForm, UserMessage


class JobFormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "date")
    list_filter = ("date", "city", "occupation")
    search_fields = ("first_name", "last_name", "email", "date")


class UserMessageAdmin(admin.ModelAdmin):
    list_display = ("user_name", "subject", "message")
    list_filter = ("user_name", "email")
    search_fields = ("user_name", "subject", "email")


admin.site.register(UserMessage, UserMessageAdmin)
admin.site.register(JobForm, JobFormAdmin)
