# Generated by Django 3.1.7 on 2021-10-15 08:43

import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211013_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='address',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='address',
            name='last_updated',
            field=main.models.AutoDateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='address',
            name='type',
            field=models.CharField(choices=[('S', 'Shipping'), ('B', 'Fakturační'), ('U', 'Neuvádět')], default='U', max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='account_status',
            field=models.IntegerField(default=1, verbose_name='Status účtu'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Jméno'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+12345678915'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Telefonní číslo'),
        ),
        migrations.AlterField(
            model_name='item',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='last_updated',
            field=main.models.AutoDateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_updated',
            field=main.models.AutoDateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]