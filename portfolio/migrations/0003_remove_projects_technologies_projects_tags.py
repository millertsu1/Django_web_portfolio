# Generated by Django 5.0.7 on 2024-08-05 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_tag_alter_projects_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='technologies',
        ),
        migrations.AddField(
            model_name='projects',
            name='tags',
            field=models.ManyToManyField(related_name='projects', to='portfolio.tag'),
        ),
    ]
