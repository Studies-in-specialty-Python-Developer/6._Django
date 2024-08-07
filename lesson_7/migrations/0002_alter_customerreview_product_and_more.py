# Generated by Django 4.2.13 on 2024-07-30 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_4', '0007_alter_user_phone'),
        ('lesson_7', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerreview',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lesson_4.product'),
        ),
        migrations.AlterField(
            model_name='customerreview',
            name='rating',
            field=models.IntegerField(choices=[(0, 'Good'), (1, 'Normal'), (2, 'Bad')]),
        ),
        migrations.AlterField(
            model_name='customerreview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lesson_4.user'),
        ),
    ]
