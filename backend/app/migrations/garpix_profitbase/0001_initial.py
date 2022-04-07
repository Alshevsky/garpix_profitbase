# Generated by Django 3.1 on 2022-04-07 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('garpix_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmptyMixin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('profitbase_id', models.IntegerField(blank=True, null=True, verbose_name='ProfitBase ID')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
                'ordering': ('title',),
            },
            bases=('garpix_page.basepage', models.Model),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('emptymixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_profitbase.emptymixin')),
                ('title', models.CharField(max_length=100, verbose_name='Название города')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'ordering': ('title',),
            },
            bases=('garpix_profitbase.emptymixin', models.Model),
        ),
        migrations.CreateModel(
            name='HouseFloor',
            fields=[
                ('emptymixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_profitbase.emptymixin')),
                ('number', models.IntegerField(blank=True, default=1, verbose_name='Номер Этажа')),
            ],
            options={
                'verbose_name': 'Этаж',
                'verbose_name_plural': 'Этажи',
            },
            bases=('garpix_profitbase.emptymixin', models.Model),
        ),
        migrations.CreateModel(
            name='HouseSection',
            fields=[
                ('emptymixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_profitbase.emptymixin')),
                ('number', models.CharField(blank=True, default='', max_length=256, verbose_name='Номер подъезда')),
            ],
            options={
                'verbose_name': 'Подьезд',
                'verbose_name_plural': 'Подьезды',
            },
            bases=('garpix_profitbase.emptymixin', models.Model),
        ),
        migrations.CreateModel(
            name='LayoutPlan',
            fields=[
                ('emptymixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_profitbase.emptymixin')),
                ('profitbase_id', models.IntegerField(blank=True, null=True, verbose_name='ProfitBase ID')),
                ('name', models.CharField(blank=True, default='LayoutPlanName', max_length=256, verbose_name='Название планировки')),
                ('is_active', models.BooleanField(default=True, verbose_name='Планировка активна?')),
                ('rooms', models.IntegerField(blank=True, default=1, verbose_name='Количество комнат')),
                ('area_total', models.FloatField(blank=True, null=True, verbose_name='Суммарная площадь')),
                ('price', models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Планировка',
                'verbose_name_plural': 'Планировки',
            },
            bases=('garpix_profitbase.emptymixin', models.Model),
        ),
        migrations.CreateModel(
            name='PropertySpecialOffer',
            fields=[
                ('emptymixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_profitbase.emptymixin')),
                ('is_active', models.BooleanField(default=False, verbose_name='Акция активна?')),
                ('title', models.CharField(blank=True, default='', max_length=256, verbose_name='Название акции')),
                ('profitbase_id', models.IntegerField(blank=True, null=True, verbose_name='ID акции')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание акции')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата начала ивента')),
                ('finish_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания ивента')),
                ('discount', models.DecimalField(decimal_places=1, default=0.0, max_digits=10, verbose_name='Скидка')),
                ('discount_type', models.CharField(choices=[('FULL_PRICE', 'Скидка на общую стоимость'), ('METER_PRICE', 'Скидка на 1 кв.м. помещения')], default='FULL_PRICE', max_length=50)),
                ('discount_unit', models.CharField(choices=[('PERCENT', '%'), ('VALUE', 'руб.')], default='PERCENT', max_length=50)),
            ],
            options={
                'verbose_name': 'Специальное предложение',
                'verbose_name_plural': 'Специальные предложения',
            },
            bases=('garpix_profitbase.emptymixin', models.Model),
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('profitbase_id', models.IntegerField(blank=True, null=True, verbose_name='ProfitBase ID')),
                ('self_project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='house', to='garpix_profitbase.project', verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Дом',
                'verbose_name_plural': 'Дома',
                'ordering': ('title',),
            },
            bases=('garpix_page.basepage', models.Model),
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
                ('profitbase_id', models.IntegerField(verbose_name='ProfitBase ID')),
                ('number', models.CharField(blank=True, default='', max_length=256, verbose_name='Номер помещения')),
                ('rooms', models.IntegerField(blank=True, default=1, verbose_name='Количество комнат')),
                ('studio', models.BooleanField(default=False, verbose_name='Студия')),
                ('free_layout', models.BooleanField(default=False, verbose_name='Свободная планировка')),
                ('euro_layout', models.BooleanField(default=False, verbose_name='Европланировка')),
                ('has_related_preset_with_layout', models.BooleanField(default=False, verbose_name='Имеет связанную предустановку с макетом')),
                ('facing', models.CharField(blank=True, max_length=350, null=True, verbose_name='Отделка')),
                ('area_total', models.FloatField(blank=True, null=True, verbose_name='Суммарная площадь')),
                ('area_estimated', models.FloatField(blank=True, null=True, verbose_name='Оценочная площадь')),
                ('area_living', models.FloatField(blank=True, null=True, verbose_name='Жилая площадь')),
                ('area_kitchen', models.FloatField(blank=True, null=True, verbose_name='Площадь кухни')),
                ('area_balcony', models.FloatField(blank=True, null=True, verbose_name='Площадь балкона/ов')),
                ('area_without_balcony', models.FloatField(blank=True, null=True, verbose_name='Площадь за вычетом балконов')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Цена')),
                ('price_per_meter', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Цена за метр')),
                ('status', models.CharField(blank=True, max_length=350, null=True, verbose_name='Статус')),
                ('self_house', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='property', to='garpix_profitbase.house', verbose_name='Дом')),
                ('floor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='property', to='garpix_profitbase.housefloor', verbose_name='Этаж на шахматке')),
                ('layout_plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='property', to='garpix_profitbase.layoutplan', verbose_name='Планировка')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='property', to='garpix_profitbase.housesection', verbose_name='Секция')),
                ('special_offer', models.ManyToManyField(blank=True, null=True, related_name='properties', to='garpix_profitbase.PropertySpecialOffer')),
            ],
            options={
                'verbose_name': 'Помещение',
                'verbose_name_plural': 'Помещения',
                'ordering': ('number',),
            },
            bases=('garpix_page.basepage', models.Model),
        ),
        migrations.AddField(
            model_name='project',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='garpix_profitbase.city', verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='layoutplan',
            name='self_house',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='layout_plan', to='garpix_profitbase.house', verbose_name='Дом'),
        ),
        migrations.AddField(
            model_name='housesection',
            name='house',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='section', to='garpix_profitbase.house', verbose_name='Дом'),
        ),
        migrations.AddField(
            model_name='housefloor',
            name='house',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='floor', to='garpix_profitbase.house', verbose_name='Дом'),
        ),
        migrations.AddField(
            model_name='housefloor',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='floor', to='garpix_profitbase.housesection', verbose_name='Секция'),
        ),
    ]