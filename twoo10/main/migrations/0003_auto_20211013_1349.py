# Generated by Django 3.1.7 on 2021-10-13 13:49

from django.db import migrations, models
import django.utils.timezone
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20211013_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='type',
            field=models.CharField(choices=[('S', 'Shipping'), ('B', 'Billing'), ('U', 'Neuvádět')], default='U', max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='account_status',
            field=models.IntegerField(default=1, verbose_name='Account status'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_of_birth',
            field=models.DateField(blank=True, verbose_name='Date of birth'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(blank=True, choices=[('F', 'Žena'), ('M', 'Muž'), ('U', 'Neuvádět')], default='U', max_length=10, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_updated',
            field=main.models.AutoDateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='surname',
            field=models.CharField(blank=True, max_length=100, verbose_name='Surname'),
        ),
    ]
