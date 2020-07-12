# Generated by Django 3.0.4 on 2020-07-07 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_dugunsalonu'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalonImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.DugunSalonu')),
            ],
        ),
    ]
