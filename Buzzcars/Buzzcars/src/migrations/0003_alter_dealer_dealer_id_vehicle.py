# Generated by Django 4.0.1 on 2022-01-14 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_alter_dealer_dealer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealer',
            name='dealer_id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicle_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('vehicle_img', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Hatchback', 'Hatchback'), ('Sedan', 'Sedan'), ('MPV', 'MPV'), ('SUV', 'SUV'), ('Crossover', 'Crossover'), ('Coupe', 'Coupe'), ('Convertible', 'Convertible')], max_length=100)),
                ('description', models.TextField(max_length=100)),
                ('cost', models.IntegerField()),
                ('status', models.CharField(choices=[('For Sale', 'For Sale'), ('Sold', 'Sold')], default='For Sale', max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('dealer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.dealer')),
            ],
        ),
    ]
