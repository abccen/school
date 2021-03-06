# Generated by Django 4.0.6 on 2022-07-06 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses_app.course')),
            ],
        ),
    ]
