# Generated by Django 3.2.9 on 2022-02-03 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20220203_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linedata',
            name='spare',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='api.spare'),
        ),
    ]
