# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-09 08:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_celery_beat', '0001_initial'),
        ('web', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('order', models.SmallIntegerField(default=1)),
                ('task_type', models.CharField(choices=[('sshtask', 'Run Shell Script'), ('scptask', 'SSH File Transfer')], max_length=64)),
                ('enabled', models.BooleanField(default=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('enabled', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bernard.Plan')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_celery_beat.PeriodicTask')),
            ],
        ),
        migrations.CreateModel(
            name='SCPTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_path', models.CharField(max_length=128)),
                ('remote_path', models.CharField(max_length=128)),
                ('bind_hosts', models.ManyToManyField(blank=True, to='web.BindHosts')),
                ('host_groups', models.ManyToManyField(blank=True, to='web.HostGroups')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bernard.Job')),
            ],
        ),
        migrations.CreateModel(
            name='SSHTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commands', models.TextField(verbose_name='ssh commands')),
                ('bind_hosts', models.ManyToManyField(blank=True, to='web.BindHosts')),
                ('host_groups', models.ManyToManyField(blank=True, to='web.HostGroups')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bernard.Job')),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Default plan', max_length=64)),
                ('order', models.SmallIntegerField(default=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bernard.Plan')),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bernard.Stage'),
        ),
    ]