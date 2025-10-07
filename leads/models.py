from django.db import models

class Lead(models.Model):
    STATUS_CHOICES = (
        ('new', 'Новый'),
        ('lost', 'Потерян'),
        ('contacted', 'Установлен контакт')
    )

    fisrt_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=25, verbose_name='Телефон')
    status = models.CharField(max_length=25,verbose_name='Статус',choices=STATUS_CHOICES,default='new')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    update_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)

    def __str__(self):
        return f"{self.fisrt_name} {self.last_name}"
    
    class Meta:
        verbose_name = 'Лид'
        verbose_name_plural = 'Лиды'
        ordering = ['-created_at']



class Client(models.Model):
    fisrt_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=25, verbose_name='Телефон')
    company_name =  models.CharField(max_length=100, verbose_name='Название компании')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    def __str__(self):
        return f"{self.fisrt_name} {self.last_name}"
    
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['-created_at']