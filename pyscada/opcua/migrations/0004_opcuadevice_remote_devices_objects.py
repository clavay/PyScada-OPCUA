# Generated by Django 2.2.8 on 2021-12-17 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opcua', '0003_auto_20211217_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='opcuadevice',
            name='remote_devices_objects',
            field=models.CharField(default='', help_text='After creating a remote device, refresh the page until you see the result', max_length=2000),
        ),
    ]