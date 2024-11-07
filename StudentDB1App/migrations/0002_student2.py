# Generated by Django 5.1.1 on 2024-09-26 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentDB1App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('marks', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.BigIntegerField()),
                ('address', models.TextField()),
            ],
        ),
    ]