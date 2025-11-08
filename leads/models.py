
from tabnanny import verbose
from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType

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
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null = True, 
        blank = True,
        verbose_name = "Менеджер"
    )

    notes = GenericRelation('Note')

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

    notes = GenericRelation('Note')

    def __str__(self):
        return f"{self.fisrt_name} {self.last_name}"
    
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['-created_at']


class Note(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name = "Автор"
    )
    content = models.TextField("Текст заметки")
    created_at=models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    # Поля для GenericForeignKey
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['-created_at']
    