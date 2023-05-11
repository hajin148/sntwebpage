# Generated by Django 4.2.1 on 2023-05-11 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_alter_dateoptions_options_alter_reservation_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=20)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='dateoptions',
            name='capacity',
        ),
        migrations.RemoveField(
            model_name='dateoptions',
            name='time_options',
        ),
        migrations.AddField(
            model_name='dateoptions',
            name='time_options',
            field=models.ManyToManyField(to='reservation.timeoption'),
        ),
    ]