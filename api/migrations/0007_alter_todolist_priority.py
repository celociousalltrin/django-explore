# Generated by Django 5.0.3 on 2024-03-29 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_tags_title_alter_todolist_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='priority',
            field=models.CharField(choices=[('low', 'Low'), ('med', 'Medium'), ('high', 'High')], default='low', max_length=6),
        ),
    ]
