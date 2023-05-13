from django.db import models

class DateOptions(models.Model):
    class Meta:
        verbose_name = '예약가능일'
        verbose_name_plural = '예약가능일'

    date = models.DateField(verbose_name="날짜")
    capacity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.date}"


class Reservation(models.Model):
    class Meta:
        verbose_name = '예약자'
        verbose_name_plural = '예약자명단'
    nameStudent = models.CharField(verbose_name="이름", max_length=100)
    school = models.CharField(verbose_name="학교",max_length=100)
    grade = models.IntegerField(verbose_name="학년",)
    class_choices = [('Current Issue', 'Current Issue'), ('Academic R & W', 'Academic R & W'), ('Debate', 'Debate'), ('Literature Review', 'Literature Review')]
    desired_class = models.CharField(verbose_name="희망수업", choices=class_choices, max_length=30)
    parents_phone_number = models.CharField(verbose_name="학부모 휴대번호", max_length=20)
    date = models.DateField(verbose_name="날짜")
    time = models.CharField(verbose_name="시간", max_length=20)