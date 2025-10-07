from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView, RedirectView
from .models import Lead, Client
# Create your views here.


class LeadListView(ListView):
# (Read) Показывает список всех лидов из таблицы
    model = Lead
    template_name = 'leads/lead_list.html'
    context_object_name = 'leads'


class LeadDetailView(DetailView):
# (Read) Показывает детальную информацию о лиде из таблицы
    model = Lead
    template_name = 'leads/lead_detail.html'
    context_object_name = 'lead'

class LeadCreateView(CreateView):
    # (Create) Создает нового лида
    model = Lead
    template_name = 'leads/lead_form.html'
    fields = ['fisrt_name', 'last_name', 'email', 'phone', 'status']
    success_url = reverse_lazy('lead-list')


class LeadUpdateView(UpdateView):
    # (Update) Обновляет существующего лида
    model = Lead
    template_name = 'leads/lead_form.html'
    fields = ['fisrt_name', 'last_name', 'email', 'phone', 'status']
    success_url = reverse_lazy('lead-list')

class LeadDeleteView(DeleteView):
# Delete Удаляет существующего лида
    model = Lead
    template_name = 'leads/lead_delete.html'
    success_url = reverse_lazy('lead-list')



# Представление класса CLIENT
class ClientListView(ListView): 
# READ Показывает список всех клиентов из таблицы
    model = Client
    template_name = 'clients/client_list.html'
    context_object_name = 'clients'

class ClientDetailView(DetailView): #Конкретный клиент
# READ Показывает детальную информацию о каждом клиенте
    model = Client
    template_name = 'clients/client_detail.html'
    context_object_name = 'client'

class ClientCreateView(CreateView): 
# Create создает нового клиента
    model = Client
    template_name = 'clients/client_form.html'
    fields = ['fisrt_name','last_name','email','phone', 'company_name']
    success_url = reverse_lazy('client-list')

class ClientUpdateView(UpdateView):
# Update - Обновляет сществующего клиента
    model  = Client
    template_name = 'client/client_form.html'
    fields = ['fisrt_name','last_name','email','phone', 'company_name']
    success_url = reverse_lazy('client-list')

class ClientDeleteView(DeleteView):
# Delete Удаляет существующего клиента
    model = Client
    template_name = 'clients/client_delete.html'
    success_url = reverse_lazy('client-list')
