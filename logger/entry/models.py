import datetime

import xlwt
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class LogEntry(models.Model):
    EXCEL_EXPORT_FIELDS = ['timestamp', 'hostname', 'message']
    EXCEL_COLUMN_WIDTH = [15, 10, 100]

    timestamp = models.DateTimeField(verbose_name=_('Timestamp'), auto_now_add=True)
    hostname = models.CharField(verbose_name=_('Hostname'), max_length=128, default=_('Unknown'))
    message = models.TextField(verbose_name=_('Message'), blank=True)

    def __str__(self):
        return _('Message from {hostname} on {timestamp}').format(hostname=self.hostname, timestamp=self.timestamp)

    @classmethod
    def export_as_excel(cls, stream, queryset=None):
        if queryset is None:
            queryset = cls.objects.all()

        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet(str(_('Exported messages')))

        # Some magic constants for widths
        for column, width in enumerate(cls.EXCEL_COLUMN_WIDTH):
            worksheet.col(column).width = 367 * width

        header_style = xlwt.easyxf('font: bold on')

        def write_cell(cell, row_index, column_index, style=None):
            if isinstance(cell, datetime.datetime):
                style = xlwt.easyxf(num_format_str='DD/MM/YYYY hh:mm:ss')
                content = cell.astimezone(timezone.get_current_timezone()).replace(tzinfo=None)
            else:
                content = str(cell)

            if style is None:
                style = xlwt.easyxf()

            worksheet.write(row_index, column_index, content, style)

        def write_row(row, row_index=0, start_col=0, style=None):
            for column_index, content in enumerate(row, start_col):
                write_cell(content, row_index, column_index, style)

        header = [str(cls._meta.get_field(field).verbose_name) for field in cls.EXCEL_EXPORT_FIELDS]
        write_row(header, style=header_style)

        row_index = 1
        for item in queryset:
            write_row([getattr(item, field) for field in cls.EXCEL_EXPORT_FIELDS], row_index)
            row_index += 1

        workbook.save(stream)

    class Meta:
        verbose_name = _('Log Entry')
        verbose_name_plural = _('Log Entries')
