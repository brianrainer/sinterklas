# Generated by Django 2.1.3 on 2018-11-16 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20181115_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='is_accepted',
            field=models.BooleanField(default=False),
        ),
    ]