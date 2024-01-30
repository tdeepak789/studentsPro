# Generated by Django 4.2.4 on 2023-09-13 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0005_remove_studentregister_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='staff',
            fields=[
                ('staff_id', models.AutoField(auto_created=True, db_index=True, max_length=5, primary_key=True, serialize=False)),
                ('staff_name', models.CharField(max_length=25)),
                ('staff_subjects', models.TextField()),
                ('staff_sections', models.CharField(max_length=12)),
            ],
        ),
        migrations.RemoveField(
            model_name='studentregister',
            name='s_age',
        ),
        migrations.AddField(
            model_name='studentregister',
            name='s_attendance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentregister',
            name='s_contact',
            field=models.CharField(default=789456, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentregister',
            name='s_feedue',
            field=models.DecimalField(decimal_places=2, default=5000, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentregister',
            name='s_class',
            field=models.IntegerField(),
        ),
    ]
