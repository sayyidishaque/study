# Generated by Django 4.2 on 2023-04-18 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statiapp', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='spimage')),
                ('disc', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='feedback',
        ),
    ]
