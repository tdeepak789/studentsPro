# Generated by Django 4.2.4 on 2023-08-15 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0003_studentregister_s_reg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentregister',
            name='s_reg',
            field=models.IntegerField(auto_created=True, db_index=True, default=123, max_length=5),
        ),
    ]