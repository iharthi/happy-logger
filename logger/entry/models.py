from django.db import models
from django.utils.translation import gettext_lazy as _


class LogEntry(models.Model):
    timestamp = models.DateTimeField(verbose_name=_('Timestamp'), auto_now_add=True)
    hostname = models.CharField(verbose_name=_('Hostname'), max_length=128, default=_('Unknown'))
    message = models.TextField(verbose_name=_('Message'), blank=True)

    def __str__(self):
        return _('Message from {hostname} on {timestamp}').format(hostname=self.hostname, timestamp=self.timestamp)

    class Meta:
        verbose_name = _('Log Entry')
        verbose_name_plural = _('Log Entries')
