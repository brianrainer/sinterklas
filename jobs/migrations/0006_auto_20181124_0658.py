# Generated by Django 2.1.3 on 2018-11-23 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_job_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employment',
            name='rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employment',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
    ]