# Generated by Django 3.2.5 on 2021-07-12 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('address', models.TextField(max_length=1000)),
                ('phonenumber', models.IntegerField()),
                ('profileimage', models.ImageField(upload_to='profileimage')),
            ],
        ),
    ]