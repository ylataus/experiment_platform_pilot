# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-25 20:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consent_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agree', models.CharField(blank=True, default=None, max_length=35, null=True)),
                ('timestamp', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Crowd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_id', models.PositiveIntegerField()),
                ('size', models.PositiveIntegerField(choices=[(3, b'_group'), (30, b'_crowd')], default=3)),
                ('communication', models.CharField(choices=[(b'_chat', b'_chat'), (b'_forum', b'_forum')], default=b'_chat', max_length=255)),
                ('creation_date', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('is_active', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Crowd_Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('cohort_id', models.PositiveIntegerField()),
                ('member_num', models.IntegerField(default=None)),
                ('crowd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='experiment.Crowd')),
            ],
        ),
        migrations.CreateModel(
            name='ExpUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, default=None, max_length=35, null=True)),
                ('expstage', models.CharField(blank=True, default=None, max_length=35, null=True)),
                ('secret_code', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProblemHint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hint_type', models.CharField(max_length=255)),
                ('candidate_1', models.CharField(max_length=255)),
                ('candidate_2', models.CharField(max_length=255)),
                ('candidate_3', models.CharField(max_length=255)),
                ('candidate_4', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_id', models.PositiveIntegerField()),
                ('version_id', models.PositiveIntegerField()),
                ('crowd_size', models.PositiveIntegerField(choices=[(3, b'_group'), (30, b'_crowd')], default=3)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileHint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_id', models.PositiveIntegerField()),
                ('version_id', models.PositiveIntegerField()),
                ('crowd_size', models.PositiveIntegerField(choices=[(3, b'_group'), (30, b'_crowd')], default=3)),
                ('hint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experiment.ProblemHint')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('worker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('GrpSol', models.TextField()),
                ('InvSolWife', models.TextField()),
                ('InvSolJob', models.TextField()),
                ('InvSolCity', models.TextField()),
                ('DegConf', models.IntegerField()),
                ('Diff', models.TextField()),
                ('GrpExp1_1', models.PositiveIntegerField()),
                ('GrpExp1_2', models.PositiveIntegerField()),
                ('GrpExp1_3', models.PositiveIntegerField()),
                ('GrpExp1_4', models.PositiveIntegerField()),
                ('GrpExp1_5', models.PositiveIntegerField()),
                ('GrpExp1_6', models.PositiveIntegerField()),
                ('GrpExp1_7', models.PositiveIntegerField()),
                ('GrpExp2', models.TextField()),
                ('Sex', models.CharField(choices=[(b'male', b'male'), (b'female', b'female')], default=b'male', max_length=35)),
                ('Age', models.PositiveIntegerField()),
                ('Edu', models.CharField(choices=[(b'less than 6', b'less than 6'), (b'less than 12', b'less than 12'), (b'high school', b'high school'), (b'some college', b'some college'), (b'undergrad', b'undergrad'), (b'masters', b'masters'), (b'doctoral', b'doctoral')], default=b'less than 6', max_length=35)),
                ('Empl_schoolFull', models.CharField(choices=[(b'yes', b'yes'), (b'no', b'no')], default=b'no', max_length=35)),
                ('Empl_schoolPart', models.CharField(choices=[(b'yes', b'yes'), (b'no', b'no')], default=b'no', max_length=35)),
                ('Empl_full', models.CharField(choices=[(b'yes', b'yes'), (b'no', b'no')], default=b'no', max_length=35)),
                ('Empl_part', models.CharField(choices=[(b'yes', b'yes'), (b'no', b'no')], default=b'no', max_length=35)),
                ('Country', models.TextField()),
                ('HITs', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TaskUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crowd', models.SlugField(max_length=35)),
                ('time_type', models.CharField(max_length=35)),
                ('time_stamp', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crowd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experiment.Crowd')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experiment.Profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='expuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='crowd_members',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='consent_form',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
