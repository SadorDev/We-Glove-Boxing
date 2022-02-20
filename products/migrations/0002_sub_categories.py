# Generated by Django 3.2.12 on 2022-02-18 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='sub_categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('display_name', models.CharField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'sub_categories',
            },
        ),
    ]