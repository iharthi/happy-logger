from django.contrib import admin

from entry.models import LogEntry
from logger.mixins import ReadOnlyAdminMixin


@admin.register(LogEntry)
class LogEntryAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    list_display = ['timestamp', 'hostname', 'message']
    list_filter = ['hostname']
    date_hierarchy = 'timestamp'
