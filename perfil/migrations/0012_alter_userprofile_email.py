# Generated by Django 5.0.6 on 2024-07-17 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0011_userprofile_sobrenome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]