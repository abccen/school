# Generated by Django 4.0.6 on 2022-07-06 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='mail@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(default='name', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('F', 'female'), ('M', 'male')], default='M', max_length=2),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(default='last name', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(max_length=13, null=True),
        ),
    ]
