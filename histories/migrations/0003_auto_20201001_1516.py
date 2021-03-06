# Generated by Django 3.1.1 on 2020-10-01 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('histories', '0002_auto_20200921_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='history',
        ),
        migrations.AddField(
            model_name='history',
            name='img_after',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='img_after', to='histories.image'),
        ),
        migrations.AddField(
            model_name='history',
            name='img_before',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='img_before', to='histories.image'),
        ),
    ]
