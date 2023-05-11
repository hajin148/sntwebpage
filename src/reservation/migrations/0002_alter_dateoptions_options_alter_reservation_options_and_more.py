# Generated by Django 4.2.1 on 2023-05-11 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dateoptions',
            options={'verbose_name': '예약가능시간', 'verbose_name_plural': '예약가능시간'},
        ),
        migrations.AlterModelOptions(
            name='reservation',
            options={'verbose_name': '예약자', 'verbose_name_plural': '예약자명단'},
        ),
        migrations.AlterField(
            model_name='reservation',
            name='desired_class',
            field=models.CharField(choices=[('Current Issue', 'Current Issue'), ('Academic R & W', 'Academic R & W'), ('Debate', 'Debate'), ('Literature Review', 'Literature Review')], max_length=30, verbose_name='희망수업'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='nameStudent',
            field=models.CharField(max_length=100, verbose_name='이름'),
        ),
    ]