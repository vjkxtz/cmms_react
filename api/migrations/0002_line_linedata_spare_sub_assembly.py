# Generated by Django 3.2.9 on 2022-02-03 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Spare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=15)),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(choices=[('ordered', 'Ordered'), ('po pending', 'Po Pending'), ('available', 'Available')], default='available', max_length=15)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('part', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='api.part')),
            ],
        ),
        migrations.CreateModel(
            name='sub_assembly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component_item', models.CharField(max_length=15)),
                ('component', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='api.spare')),
                ('part', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='api.part')),
            ],
        ),
        migrations.CreateModel(
            name='LineData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workdone', models.CharField(max_length=150)),
                ('date', models.DateField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('line', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='api.line')),
                ('part', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='api.part')),
                ('sub_assembly', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='api.sub_assembly')),
            ],
        ),
    ]
