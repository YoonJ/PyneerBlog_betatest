# Generated by Django 2.1 on 2018-08-06 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_member',
            field=models.TextField(default='No one'),
        ),
    ]