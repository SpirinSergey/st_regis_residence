# Generated by Django 4.0.2 on 2022-02-08 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='Last name')),
                ('phone', models.CharField(blank=True, max_length=150, verbose_name='Phone')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('date', models.CharField(blank=True, max_length=50, verbose_name='Date and time')),
                ('agent_type', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], max_length=150, verbose_name='Is a realtor')),
                ('date_creation', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date creation')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Book an appointments',
            },
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='Last name')),
                ('phone', models.CharField(blank=True, max_length=150, verbose_name='Phone')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('agent_type', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], max_length=150, verbose_name='Is a realtor')),
                ('date_creation', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date creation')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Feedbacks',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_img', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FLOOR', models.IntegerField(default=0)),
                ('UNIT_TYPE', models.CharField(max_length=20, null=True)),
                ('BATHROOMS', models.CharField(max_length=5, null=True)),
                ('UNIT', models.IntegerField(default=0)),
                ('INTERIOR', models.CharField(max_length=25, null=True)),
                ('TERRACE', models.CharField(max_length=25, null=True)),
                ('TOTAL', models.CharField(max_length=25, null=True)),
                ('PRICE', models.CharField(max_length=25, null=True)),
                ('FLOOR_PLANE', models.FileField(blank=True, upload_to='floor_plane/')),
            ],
        ),
    ]
