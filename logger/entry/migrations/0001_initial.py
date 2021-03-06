# Generated by Django 2.2.4 on 2019-08-16 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')),
                ('hostname', models.CharField(default='Unknown', max_length=128, verbose_name='Hostname')),
                ('message', models.TextField(blank=True, verbose_name='Message')),
            ],
        ),
    ]
