# Generated by Django 3.0.5 on 2021-05-31 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safarisapp', '0003_auto_20210531_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartmentsbase',
            name='Beds',
            field=models.PositiveSmallIntegerField(default=0, max_length=1),
        ),
        migrations.AddField(
            model_name='apartmentsbase',
            name='Category',
            field=models.CharField(choices=[('DEL', 'DL1'), ('Rook', 'RK1'), ('Bishop', 'BP1'), ('Castle', 'CST1')], default=0, max_length=11),
        ),
    ]
