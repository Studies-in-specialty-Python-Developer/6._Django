# Generated by Django 4.2.13 on 2024-07-30 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_7', '0002_alter_customerreview_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerreview',
            name='product',
        ),
        migrations.RemoveField(
            model_name='customerreview',
            name='user',
        ),
        migrations.AddField(
            model_name='customerreview',
            name='product_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customerreview',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]