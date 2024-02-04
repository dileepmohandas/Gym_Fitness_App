# Generated by Django 5.0.1 on 2024-02-04 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0003_membershipplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Selectdate', models.DateTimeField(auto_now_add=True)),
                ('phonenumber', models.CharField(max_length=15)),
                ('Login', models.CharField(max_length=200)),
                ('Logout', models.CharField(max_length=200)),
                ('SelectWorkout', models.CharField(max_length=200)),
                ('TrainedBy', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='gallery')),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='Price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='membershipplan',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='salary',
            field=models.IntegerField(),
        ),
    ]