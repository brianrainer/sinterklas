# Generated by Django 2.1.3 on 2018-11-10 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='created_at',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='created_at',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='updated_at',
            new_name='date_modified',
        ),
        migrations.RemoveField(
            model_name='job',
            name='company',
        ),
        migrations.AddField(
            model_name='job',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
