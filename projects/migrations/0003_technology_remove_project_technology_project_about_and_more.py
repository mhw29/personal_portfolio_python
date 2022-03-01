# Generated by Django 4.0.2 on 2022-02-27 14:59

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180)),
                ('image', models.FilePathField(blank=True, default=None, null=True, path='C:\\Development\\mwilliamson_portfolio_python\\mwilliamson_portfolio_python\\img')),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='technology',
        ),
        migrations.AddField(
            model_name='project',
            name='about',
            field=ckeditor.fields.RichTextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='metrics',
            field=ckeditor.fields.RichTextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='my_role',
            field=ckeditor.fields.RichTextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='process',
            field=ckeditor.fields.RichTextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='result',
            field=ckeditor.fields.RichTextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(blank=True, default=None, null=True, path='C:\\Development\\mwilliamson_portfolio_python\\mwilliamson_portfolio_python\\img'),
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(to='projects.Technology'),
        ),
    ]