from django.contrib import admin
from .models import Lead, Client, Note
# Register your models here.
@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('fisrt_name', 'last_name', 'email', 'status', 'phone')
    list_filter = ('status', 'manager')
    search_fields = ('fisrt_name', 'last_name', 'email')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('fisrt_name', 'last_name', 'email', 'phone','company_name')
    list_filter = ('company_name',)
    search_fields = ('fisrt_name', 'last_name', 'email')


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_at')
    list_filter = ('author',)
    search_fields = ('author', 'content')

