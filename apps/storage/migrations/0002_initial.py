# Generated by Django 3.2.9 on 2021-11-23 10:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PREORDER', 'Не оплачен'), ('ORDER', 'Оплачен'), ('DONE', 'Завершён')], default='PREORDER', max_length=10, verbose_name='Статус заказа')),
                ('access_code', models.CharField(max_length=50, unique=True, verbose_name='Код доступа')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='PricePeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.CharField(max_length=100, verbose_name='Единица времени')),
            ],
            options={
                'verbose_name': 'Базовое время аренды',
                'verbose_name_plural': 'Базовое время аренды',
                'db_table': 'price_periods',
            },
        ),
        migrations.CreateModel(
            name='UnitMeasurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Единица измерения')),
            ],
            options={
                'verbose_name': 'Единица измерения',
                'verbose_name_plural': 'Единицы измерения',
                'db_table': 'unit_measurements',
            },
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название склада')),
                ('description', models.TextField(verbose_name='Подробное описание склада')),
                ('address', models.CharField(max_length=200, unique=True, verbose_name='Адрес склада')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(help_text='Введите номер телефона, например, +79999999999', max_length=128, region=None, verbose_name='Телефонный номер склада')),
                ('latitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-90, 'Широта должна быть в диапазоне от -90 до 90'), django.core.validators.MaxValueValidator(90, 'Широта должна быть в диапазоне от -90 до 90')], verbose_name='Широта')),
                ('longitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-180, 'Долгота должна быть в диапазоне от -180 до 180'), django.core.validators.MaxValueValidator(180, 'Долгота должна быть в диапазоне от -180 до 180')], verbose_name='Долгота')),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Склад',
                'verbose_name_plural': 'Склады',
                'db_table': 'warehouses',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Объект аренды')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='storage.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Объект аренды',
                'verbose_name_plural': 'Объекты аренды',
                'db_table': 'units',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='period', to='storage.priceperiod', verbose_name='Период')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rent_unit', to='storage.unit', verbose_name='Объект аренды')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storage', to='storage.warehouse', verbose_name='Склад')),
            ],
            options={
                'verbose_name': 'Цена',
                'verbose_name_plural': 'Цены',
                'db_table': 'prices',
            },
        ),
        migrations.CreateModel(
            name='OrderUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=1, verbose_name='Количество')),
                ('rent_start', models.DateField(default=django.utils.timezone.now, null=True, verbose_name='Дата начала аренды')),
                ('rent_duration', models.CharField(choices=[('1week', '1 неделя'), ('2weeks', '2 недели'), ('3weeks', '3 недели'), ('1month', '1 месяц'), ('2months', '2 месяца'), ('3months', '3 месяца'), ('4months', '4 месяца'), ('5months', '5 месяцев'), ('6months', '6 месяцев'), ('7months', '7 месяцев'), ('8months', '8 месяцев'), ('9months', '9 месяцев'), ('10months', '10 месяцев'), ('11months', '11 месяцев'), ('12months', '12 месяцев')], default='1month', max_length=10, verbose_name='Длительность аренды')),
                ('price', models.FloatField(editable=False, null=True, verbose_name='Цена')),
                ('order', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='rent_order', to='storage.order', verbose_name='Основной заказ')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='unit', to='storage.unit', verbose_name='Объект аренды')),
                ('warehouse', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='warehouse', to='storage.warehouse', verbose_name='Склад')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='measurement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mes_name', to='storage.unitmeasurement', verbose_name='Единица измерения'),
        ),
        migrations.CreateModel(
            name='BaseCategoryPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='Базовая цена')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price', to='storage.category', verbose_name='Категория')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_storage', to='storage.warehouse', verbose_name='Склад')),
            ],
            options={
                'verbose_name': 'Базовая цена',
                'verbose_name_plural': 'Базовые цены',
                'db_table': 'base_prices',
                'unique_together': {('category', 'warehouse')},
            },
        ),
    ]
