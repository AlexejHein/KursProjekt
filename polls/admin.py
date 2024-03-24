from django.contrib import admin
from .models import Poll, Choice


class PollAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'publish_time', 'days_running')


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
