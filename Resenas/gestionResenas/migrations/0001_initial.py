# Generated by Django 4.2 on 2023-05-01 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Resena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('product', models.CharField(max_length=30)),
                ('purchase_place', models.CharField(blank=True, max_length=30, null=True)),
                ('used_time', models.CharField(blank=True, max_length=10, null=True)),
                ('status', models.BinaryField()),
                ('product_valoration', models.IntegerField()),
                ('resena_valoration', models.IntegerField()),
                ('Image', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=255)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='gestionResenas.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('id_resena', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='gestionResenas.resena')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='gestionResenas.user')),
            ],
        ),
    ]
