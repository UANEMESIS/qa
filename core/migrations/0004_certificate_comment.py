# Generated by Django 3.0.3 on 2020-03-06 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200306_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='comment',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
