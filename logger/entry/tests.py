import io

from django.test import Client, TestCase, override_settings
from django.urls import reverse

from entry.models import LogEntry


class ExcelExportTestCase(TestCase):
    def setUp(self):
        LogEntry.objects.create(hostname="Unknown", message="Message 1")
        LogEntry.objects.create(hostname="Unknown", message="Message 2")
        LogEntry.objects.create(hostname="Unknown", message="Message 3")
        LogEntry.objects.create(hostname="Known", message="Message 4")

    def test_excel_export_all(self):
        stream = io.BytesIO()
        LogEntry.export_as_excel(stream)

        self.assertNotEqual(len(stream.getbuffer()), 0)

    def test_excel_export_some(self):
        stream = io.BytesIO()
        LogEntry.export_as_excel(stream, LogEntry.objects.filter(hostname="Unknown"))

        self.assertNotEqual(len(stream.getbuffer()), 0)

    def test_excel_export_none(self):
        stream = io.BytesIO()
        LogEntry.export_as_excel(stream, LogEntry.objects.none())

        self.assertNotEqual(len(stream.getbuffer()), 0)


class CreateLogEntryTestCase(TestCase):
    @override_settings(LOGGER_SECURITY_TOKEN='secret')
    def test_create_log_entry_with_auth(self):
        client = Client(
            **{
                'HTTP_X_LOGGER_TOKEN': 'secret',
                'HTTP_X_LOGGER_HOSTNAME': 'test',
            }
        )

        test_message = "Привет счастливый логгер"

        response = client.post(
            reverse('receive-message'),
            data=test_message.encode('utf-8'),
            content_type='text/plain',
        )

        # One object should be created
        self.assertEqual(response.status_code, 200)
        self.assertEqual(LogEntry.objects.count(), 1)
        self.assertEqual(LogEntry.objects.first().message, test_message)

    @override_settings(LOGGER_SECURITY_TOKEN='')
    def test_create_log_entry_no_auth(self):
        client = Client(
            **{
                'HTTP_X_LOGGER_HOSTNAME': 'test',
            }
        )

        test_message = "Привет счастливый логгер"

        response = client.post(
            reverse('receive-message'),
            data=test_message.encode('utf-8'),
            content_type='text/plain',
        )

        # One object should be created
        self.assertEqual(response.status_code, 200)
        self.assertEqual(LogEntry.objects.count(), 1)
        self.assertEqual(LogEntry.objects.first().message, test_message)

    @override_settings(LOGGER_SECURITY_TOKEN='secret')
    def test_create_log_entry_fails_with_no_auth(self):
        client = Client(
            **{
                'HTTP_X_LOGGER_HOSTNAME': 'test',
            }
        )

        test_message = "Привет счастливый логгер"

        response = client.post(
            reverse('receive-message'),
            data=test_message.encode('utf-8'),
            content_type='text/plain',
            **{
                'HTTP_X_LOGGER_HOSTNAME': 'test',
            }
        )

        # Nothing should be created due to authentication failure
        self.assertEqual(response.status_code, 403)
        self.assertEqual(LogEntry.objects.count(), 0)
