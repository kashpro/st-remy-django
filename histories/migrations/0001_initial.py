# Generated by Django 3.1.1 on 2020-09-19 13:08

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('desc', models.TextField(verbose_name='Описание')),
                ('desc_comment', models.TextField(blank=True, null=True, verbose_name='Комментарий к описанию')),
                ('desc_status', models.CharField(choices=[('mod', 'На модерации'), ('pub', 'Опубликовано'), ('reject', 'Отклонено'), ('edit', 'Редактируется')], default='mod', max_length=10, verbose_name='Статус описания')),
                ('orientation', models.CharField(choices=[('vertical', 'Вертикальная'), ('horizontal', 'Горизонтальная')], default='horiz', max_length=10, verbose_name='Ориентация')),
                ('status', models.CharField(choices=[('mod', 'На модерации'), ('pub', 'Опубликовано'), ('reject', 'Отклонено')], default='mod', max_length=10, verbose_name='Статус истории')),
                ('week', models.DateField(verbose_name='Неделя')),
                ('admin_viewed', models.BooleanField(default=False, verbose_name='Просмотренно админом')),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'История',
                'verbose_name_plural': 'Истории',
            },
        ),
        migrations.CreateModel(
            name='Voice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voices', to='histories.history', verbose_name='История')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Голос',
                'verbose_name_plural': 'Голоса',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('surname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('phone', models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message='Введен номер мобильного телефона в неправильном формате!', regex='^[0-9]{10,15}$')], verbose_name='Телефон')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='Город')),
                ('social_name', models.CharField(blank=True, choices=[('vk', 'Вконтакте'), ('ok', 'Одноклассники'), ('fb', 'Facebook')], max_length=32, null=True, verbose_name='Соц. сеть')),
                ('social_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='ID в соц. сети')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('week', models.DateField(verbose_name='Неделя')),
                ('main', models.BooleanField(default=False, verbose_name='Главный победитель')),
                ('history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='histories.history', verbose_name='История')),
            ],
            options={
                'verbose_name': 'Список победителей',
                'verbose_name_plural': 'Списки победителей',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='images/', verbose_name='Изображение')),
                ('date', models.PositiveSmallIntegerField(default=2019, verbose_name='Дата фотографии')),
                ('status', models.CharField(choices=[('mod', 'На модерации'), ('pub', 'Опубликовано'), ('reject', 'Отклонено'), ('edit', 'Редактируется')], default='mod', max_length=10, verbose_name='Статус изображения')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='histories.history', verbose_name='История')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
