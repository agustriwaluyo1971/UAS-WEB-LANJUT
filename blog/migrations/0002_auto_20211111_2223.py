# Generated by Django 3.2.8 on 2021-11-12 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artikel',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Artikel'},
        ),
        migrations.AlterModelOptions(
            name='kategori',
            options={'verbose_name_plural': 'Kategori'},
        ),
    ]
