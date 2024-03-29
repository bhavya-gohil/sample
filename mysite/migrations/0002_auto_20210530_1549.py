# Generated by Django 3.2.3 on 2021-05-30 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10000),
        ),
        migrations.AlterField(
            model_name='site',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
