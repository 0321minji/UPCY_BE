# Generated by Django 4.0 on 2024-03-27 12:53

from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_user_contest_ability_user_contest_certification_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='area',
        ),
        migrations.RemoveField(
            model_name='user',
            name='career_ability',
        ),
        migrations.RemoveField(
            model_name='user',
            name='career_certification',
        ),
        migrations.RemoveField(
            model_name='user',
            name='contest_ability',
        ),
        migrations.RemoveField(
            model_name='user',
            name='contest_certification',
        ),
        migrations.RemoveField(
            model_name='user',
            name='etc_ability',
        ),
        migrations.RemoveField(
            model_name='user',
            name='etc_certification',
        ),
        migrations.RemoveField(
            model_name='user',
            name='freelancer_ability',
        ),
        migrations.RemoveField(
            model_name='user',
            name='freelancer_certification',
        ),
        migrations.RemoveField(
            model_name='user',
            name='license_ability',
        ),
        migrations.RemoveField(
            model_name='user',
            name='license_certification',
        ),
        migrations.RemoveField(
            model_name='user',
            name='links',
        ),
        migrations.RemoveField(
            model_name='user',
            name='market_intro',
        ),
        migrations.RemoveField(
            model_name='user',
            name='market_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='school_ability',
        ),
        migrations.RemoveField(
            model_name='user',
            name='school_certification',
        ),
        migrations.RemoveField(
            model_name='user',
            name='special_material',
        ),
        migrations.RemoveField(
            model_name='user',
            name='thumbnail_image',
        ),
        migrations.RemoveField(
            model_name='user',
            name='work_style',
        ),
        migrations.CreateModel(
            name='ReformerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('links', models.TextField(blank=True, null=True)),
                ('market_name', models.CharField(blank=True, max_length=50, null=True)),
                ('market_intro', models.TextField(blank=True, null=True)),
                ('thumbnail_image', models.ImageField(blank=True, null=True, upload_to=users.models.get_upload_path)),
                ('school', models.CharField(blank=True, max_length=100, null=True)),
                ('major', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('school_certification', models.FileField(null=True, upload_to='')),
                ('special_material', models.ManyToManyField(blank=True, related_name='reformers', to='users.Material')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reformer_profile', to='users.user')),
                ('work_style', models.ManyToManyField(blank=True, related_name='styled_refomers', to='users.Style')),
            ],
        ),
        migrations.CreateModel(
            name='Outsourcing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('client', models.CharField(max_length=100)),
                ('main_tasks', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('period', models.DurationField()),
                ('proof_document', models.FileField(upload_to='')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outsourcing', to='users.reformerprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('period', models.DurationField()),
                ('proof_document', models.FileField(upload_to='')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='internship', to='users.reformerprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Freelancer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='freelancer', to='users.reformerprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('organizer', models.CharField(max_length=100)),
                ('award_date', models.DateField()),
                ('proof_document', models.FileField(upload_to='')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competition', to='users.reformerprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('issuing_authority', models.CharField(max_length=100)),
                ('issue_date', models.DateField()),
                ('proof_document', models.FileField(upload_to='')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certification', to='users.reformerprofile')),
            ],
        ),
    ]
