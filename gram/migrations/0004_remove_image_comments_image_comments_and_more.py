# Generated by Django 4.0.3 on 2022-04-03 14:35

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0003_alter_image_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='comments',
        ),
        migrations.AddField(
            model_name='image',
            name='comments',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gram.comments'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profilePhoto',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='images/'),
        ),
    ]
