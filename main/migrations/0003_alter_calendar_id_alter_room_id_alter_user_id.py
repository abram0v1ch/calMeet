# Generated by Django 4.1.2 on 2022-10-16 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_calendar_file_calendar_url_alter_room_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.CharField(default='JZF7A', max_length=5, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
