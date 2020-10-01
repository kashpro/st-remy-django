# Generated by Django 3.1.1 on 2020-10-01 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('histories', '0003_auto_20201001_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='history',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='histories.history', verbose_name='История'),
        ),
    ]