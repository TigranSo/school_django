# Generated by Django 4.2.1 on 2023-12-31 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_activity_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zanyatie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='занятие')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Занятие',
            },
        ),
        migrations.AlterField(
            model_name='teacher',
            name='tel',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='телефон'),
        ),
        migrations.AddField(
            model_name='activity',
            name='zanyat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.zanyatie', verbose_name='Какое занятие ?'),
        ),
    ]
