# Generated by Django 3.0.4 on 2020-07-04 08:59

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20200701_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='danisman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=30)),
                ('soyisim', models.CharField(max_length=20)),
                ('telefon', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('detail', ckeditor_uploader.fields.RichTextUploadingField()),
                ('skype', models.CharField(max_length=50)),
            ],
        ),
    ]
