from django.contrib import admin
from django.http import HttpResponse
from django.utils.datetime_safe import datetime
from django.utils.translation import gettext_lazy as _

from entry.models import LogEntry
from logger.mixins import ReadOnlyAdminMixin


@admin.register(LogEntry)
class LogEntryAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    list_display = ['timestamp', 'hostname', 'message']
    list_filter = ['hostname']
    date_hierarchy = 'timestamp'
    actions = ['export_excel']

    def export_excel(self, request, queryset):
        response = HttpResponse(content_type="application/ms-excel")
        response['Content-Disposition'] = 'attachment; filename=LogExport-{timestamp}.xls'.format(
            timestamp=datetime.now(),
        )
        LogEntry.export_as_excel(response, queryset)
        return response
    export_excel.short_description = _("Export selected to excel")
