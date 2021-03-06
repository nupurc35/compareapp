# Generated by Django 3.2.3 on 2021-06-03 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210601_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='Battery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('fast_charging', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modules', models.CharField(max_length=50)),
                ('features', models.CharField(max_length=50)),
                ('video', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Connectivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wlan', models.CharField(max_length=50)),
                ('bluetooth', models.CharField(max_length=50)),
                ('gps', models.CharField(max_length=50)),
                ('nfc', models.CharField(max_length=50)),
                ('infrared', models.CharField(max_length=50)),
                ('radio', models.CharField(max_length=50)),
                ('usb', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Dimension',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.FloatField()),
                ('width', models.FloatField()),
                ('height', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Launch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announced_date', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=50)),
                ('price', models.FloatField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_slot', models.CharField(max_length=200)),
                ('internal_memory', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operating_system', models.CharField(max_length=200)),
                ('chipset', models.CharField(max_length=200)),
                ('cpu', models.CharField(max_length=200)),
                ('gpu', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Resolution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='smartphone',
            name='name',
        ),
        migrations.RemoveField(
            model_name='smartphone',
            name='price',
        ),
        migrations.AddField(
            model_name='smartphone',
            name='picture',
            field=models.ImageField(default='', upload_to='pics'),
        ),
        migrations.CreateModel(
            name='Display',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_type', models.CharField(max_length=200)),
                ('sizescreen', models.FloatField()),
                ('resolution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.resolution')),
            ],
        ),
        migrations.CreateModel(
            name='Body',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight_gram', models.IntegerField()),
                ('build', models.CharField(max_length=200)),
                ('sim_card', models.CharField(max_length=200)),
                ('dimension', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.dimension')),
            ],
        ),
        migrations.AddField(
            model_name='smartphone',
            name='battery',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.battery'),
        ),
        migrations.AddField(
            model_name='smartphone',
            name='body',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.body'),
        ),
        migrations.AddField(
            model_name='smartphone',
            name='connectivity',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.connectivity'),
        ),
        migrations.AddField(
            model_name='smartphone',
            name='display',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.display'),
        ),
        migrations.AddField(
            model_name='smartphone',
            name='launch',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.launch'),
        ),
        migrations.AddField(
            model_name='smartphone',
            name='main_camera',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='main_cameratocamera', to='accounts.camera'),
        ),
        migrations.AddField(
            model_name='smartphone',
            name='memory',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.memory'),
        ),
        migrations.AddField(
            model_name='smartphone',
            name='platform',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.platform'),
        ),
        migrations.AddField(
            model_name='smartphone',
            name='selfie_camera',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='selfie_cameratocamera', to='accounts.camera'),
        ),
    ]
