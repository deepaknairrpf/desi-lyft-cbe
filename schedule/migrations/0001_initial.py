# Generated by Django 2.1.5 on 2019-01-19 02:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.model


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LyfteeSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_lat', models.FloatField()),
                ('source_long', models.FloatField()),
                ('destination_lat', models.FloatField()),
                ('destination_long', models.FloatField()),
                ('scheduled_time', models.DateTimeField()),
                ('is_allocated', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_valid', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LyfterService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_lat', models.FloatField()),
                ('source_long', models.FloatField()),
                ('destination_lat', models.FloatField()),
                ('destination_long', models.FloatField()),
                ('lyftee_max_limit', models.PositiveIntegerField(default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PoolRide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_ride_completed', models.BooleanField(default=False)),
                ('lyftee_rating', utils.model.IntegerRangeField(null=True)),
                ('lyfter_rating', utils.model.IntegerRangeField(null=True)),
                ('pickup_point_lat', models.FloatField()),
                ('pickup_point_long', models.FloatField()),
                ('drop_point_lat', models.FloatField()),
                ('drop_point_long', models.FloatField()),
                ('timestamp', models.DateTimeField()),
                ('lyftee_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.LyfteeSchedule')),
                ('lyfter_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.LyfterService')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='poolride',
            unique_together={('lyftee_schedule', 'lyfter_service')},
        ),
    ]
