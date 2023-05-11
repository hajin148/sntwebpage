# Generated by Django 4.2.1 on 2023-05-11 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DateOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('capacity', models.IntegerField()),
                ('time_options', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameStudent', models.CharField(max_length=100, verbose_name='학생이름')),
                ('school', models.CharField(max_length=100, verbose_name='학교')),
                ('grade', models.IntegerField(verbose_name='학년')),
                ('desired_class', models.CharField(choices=[('C', 'C'), ('A', 'A'), ('D', 'D'), ('L', 'L')], max_length=1, verbose_name='희망수업')),
                ('parents_phone_number', models.CharField(max_length=20, verbose_name='학부모 휴대번호')),
                ('date', models.DateField(verbose_name='날짜')),
                ('time', models.CharField(max_length=20, verbose_name='시간')),
            ],
        ),
    ]