# Generated by Django 4.2.13 on 2024-05-29 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0014_alter_trainer_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='department',
            field=models.CharField(choices=[('b', 'Backend'), ('f', 'Frontend'), ('n', 'Network')], max_length=20, null=True),
        ),
    ]
