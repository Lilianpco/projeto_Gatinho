# Generated by Django 3.0.2 on 2020-01-13 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dono', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dono',
            name='endereco',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]