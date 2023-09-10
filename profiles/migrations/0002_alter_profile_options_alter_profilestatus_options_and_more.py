# Generated by Django 4.2.5 on 2023-09-10 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name_plural': 'Profiles'},
        ),
        migrations.AlterModelOptions(
            name='profilestatus',
            options={'verbose_name_plural': 'Profile Statuses'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/%Y/%m/'),
        ),
    ]