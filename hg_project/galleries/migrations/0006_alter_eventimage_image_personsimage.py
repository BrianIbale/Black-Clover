# Generated by Django 5.0.6 on 2024-05-09 00:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0005_alter_eventimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventimage',
            name='image',
            field=models.ImageField(upload_to='events/'),
        ),
        migrations.CreateModel(
            name='PersonsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='persons/')),
                ('title', models.CharField(max_length=150)),
                ('sub_title', models.CharField(max_length=100)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galleries.person')),
            ],
        ),
    ]
