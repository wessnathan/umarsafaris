# Generated by Django 3.0.5 on 2021-06-02 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='umarsafarisrooms',
            name='Name',
            field=models.CharField(default='Enter name of apartment', max_length=100),
        ),
    ]