# Generated by Django 5.1.1 on 2024-12-31 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exercise',
            options={'verbose_name': '動作', 'verbose_name_plural': '動作'},
        ),
        migrations.AlterModelOptions(
            name='workoutsession',
            options={'ordering': ('-date',), 'verbose_name': '訓練記錄', 'verbose_name_plural': '訓練記錄'},
        ),
    ]