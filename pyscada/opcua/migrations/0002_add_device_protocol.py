# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-24 12:49
from __future__ import unicode_literals
from pyscada.opcua import PROTOCOL_ID

from django.db import migrations


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    DeviceProtocol = apps.get_model("pyscada", "DeviceProtocol")
    db_alias = schema_editor.connection.alias
    if not DeviceProtocol.objects.using(db_alias).filter(pk=PROTOCOL_ID):
        DeviceProtocol.objects.using(db_alias).bulk_create([
            DeviceProtocol(pk=PROTOCOL_ID,
                           protocol='opcua',
                           description='OPCUA Interface',
                           app_name='pyscada.opcua',
                           device_class='pyscada.opcua.device',
                           daq_daemon=True,
                           single_thread=True),
        ])


def reverse_func(apps, schema_editor):
    # forwards_func() creates two Country instances,
    # so reverse_func() should delete them.
    DeviceProtocol = apps.get_model("pyscada", "DeviceProtocol")
    db_alias = schema_editor.connection.alias
    DeviceProtocol.objects.using(db_alias).filter(protocol="opcua").delete()


class Migration(migrations.Migration):
    dependencies = [
        ('opcua', '0001_initial'),
        ('pyscada', '0059_auto_20200211_1049'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]