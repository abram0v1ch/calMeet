# Generated by Django 4.1.2 on 2022-10-16 20:18

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_room_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.CharField(default=main.models.generate_id_length, max_length=5, primary_key=True, serialize=False),
        ),
    ]