from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from leads.forms import NoteForm
from .models import Lead, Client
from django.shortcuts import get_object_or_404
# Create your views here.


class OwnerRequiredMixin(UserPassesTestMixin):
    def test_function(self):
        obj = self.get_object()
        return obj.manager == self.request.user


class LeadListView(LoginRequiredMixin,ListView):
# (Read) Показывает список всех лидов из таблицы
    model = Lead
    template_name = 'leads/lead_list.html'
    context_object_name = 'leads'

    def get_queryset(self):
        return Lead.objects.filter(manager=self.request.user)


class LeadDetailView(LoginRequiredMixin, OwnerRequiredMixin,DetailView):
# (Read) Показывает детальную информацию о лиде из таблицы
    model = Lead
    template_name = 'leads/lead_detail.html'
    context_object_name = 'lead'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = self.object.notes.all()
        context['note_form'] = NoteForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = NoteForm(request.POST)

        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.content_object = self.object
            note.save()
            return self.get(request, *args, **kwargs)

        context = self.get_context_data()
        context['note_form'] = form
        return self.render_to_response(context)


class LeadCreateView(LoginRequiredMixin,CreateView):
    # (Create) Создает нового лида
    model = Lead
    template_name = 'leads/lead_form.html'
    fields = ['fisrt_name', 'last_name', 'email', 'phone', 'status']
    success_url = reverse_lazy('lead-list')

    def form_valid(self, form):
        form.instance.manager = self.request.user
        return super().form_valid(form)


class LeadUpdateView(LoginRequiredMixin,OwnerRequiredMixin,UpdateView):
    # (Update) Обновляет существующего лида
    model = Lead
    template_name = 'leads/lead_form.html'
    fields = ['fisrt_name', 'last_name', 'email', 'phone', 'status']
    success_url = reverse_lazy('lead-list')

class LeadDeleteView(LoginRequiredMixin,OwnerRequiredMixin,DeleteView):
# Delete Удаляет существующего лида
    model = Lead
    template_name = 'leads/lead_delete.html'
    success_url = reverse_lazy('lead-list')


class LeadConvertView(LoginRequiredMixin,OwnerRequiredMixin,RedirectView):
    permanent = False
    def get_redirect_url(self, *args, **kwargs):
        lead = get_object_or_404(Lead, pk=kwargs['pk'] )
        # Создаем нового клиента, перенося данные
        client = Client.objects.create(
            fisrt_name = lead.fisrt_name,
            last_name = lead.last_name,
            phone = lead.phone,
            email = lead.email
        )
        lead.delete()
        return reverse_lazy('client-detail', kwargs={'pk':client.pk})



# Представление класса CLIENT
class ClientListView(LoginRequiredMixin,ListView): 
# READ Показывает список всех клиентов из таблицы
    model = Client
    template_name = 'clients/client_list.html'
    context_object_name = 'clients'

class ClientDetailView(LoginRequiredMixin,DetailView): #Конкретный клиент
# READ Показывает детальную информацию о каждом клиенте
    model = Client
    template_name = 'clients/client_detail.html'
    context_object_name = 'client'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = self.object.notes.all()
        context['note_form'] = NoteForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = NoteForm(request.POST)

        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.content_object = self.object
            note.save()
            return self.get(request, *args, **kwargs)

        context = self.get_context_data()
        context['note_form'] = form
        return self.render_to_response(context)


class ClientCreateView(LoginRequiredMixin,CreateView): 
# Create создает нового клиента
    model = Client
    template_name = 'clients/client_form.html'
    fields = ['fisrt_name','last_name','email','phone', 'company_name']
    success_url = reverse_lazy('client-list')

class ClientUpdateView(LoginRequiredMixin,UpdateView):
# Update - Обновляет сществующего клиента
    model  = Client
    template_name = 'clients/client_form.html'
    fields = ['fisrt_name','last_name','email','phone', 'company_name']
    success_url = reverse_lazy('client-list')

class ClientDeleteView(LoginRequiredMixin,DeleteView):
# Delete Удаляет существующего клиента
    model = Client
    template_name = 'clients/client_delete.html'
    success_url = reverse_lazy('client-list')
