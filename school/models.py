from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    name = models.CharField(max_length=100, verbose_name='преподаватель')
    name_prof = models.CharField(max_length=100, verbose_name='профессия')
    tel = models.CharField(max_length=60, blank=True, null=True, verbose_name='телефон')
    description = models.TextField(blank=True, verbose_name='Информация')
    img_main = models.ImageField(upload_to='img', blank=False, verbose_name='Фото')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'преподаватель'

    def __str__(self):
        return f"{self.name}"

class Zanyatie(models.Model):
    name = models.CharField(max_length=100, verbose_name='занятие')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Вид занятии'

    def __str__(self):
        return f"{self.name}"


class Activity(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,  verbose_name='преподаватель')
    name = models.CharField(max_length=100, verbose_name='Название занятия')
    description = models.TextField(verbose_name='Информация')
    zanyat = models.ForeignKey(Zanyatie, on_delete=models.CASCADE, blank=True, null=True,  verbose_name='Какое занятие ?')
    price = models.DecimalField(max_digits=10, blank=True, null=True, decimal_places=2, verbose_name='Цена занятия')
    img_main = models.ImageField(upload_to='img', blank=False, verbose_name='Главная картина')
    img_1 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_2 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_3 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_4 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    img_5 = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Дополнительная картина')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Занятия'

    def __str__(self):
        return f"{self.name}"


class Schedule(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        verbose_name_plural = 'расписания занятий'

    def __str__(self):
        return f"{self.activity} - {self.date} {self.time}"
    

class Enrollment(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name='Название занятия')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,verbose_name='Преподаватель')
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    comments = models.TextField(verbose_name='Комментарии')

    class Meta:
        verbose_name_plural = 'Записи на занятии'

    def __str__(self):
        return f"{self.activity} - {self.date} {self.time}"
