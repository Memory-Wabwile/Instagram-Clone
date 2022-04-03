# Generated by Django 4.0.3 on 2022-04-01 12:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilePhoto', models.ImageField(default='', upload_to='media/')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=150)),
                ('bio', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='media/')),
                ('imageName', models.CharField(max_length=70)),
                ('imageCaption', models.TextField(max_length=65)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('comments', models.ManyToManyField(default=False, to='gram.comments')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gram.profile')),
            ],
        ),
    ]