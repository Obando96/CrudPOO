from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from crudContactos.models import Contactos

# Create your views here.
class ContactListView(generic.ListView):
    model = Contactos


class ContactCreateView(generic.CreateView):
    model = Contactos # Redirect to home after successful creation
    fields = ['nombre', 'email', 'birthdate', 'phone']
    success_url = reverse_lazy('crudContact_list')


class ContactUpdateView(generic.UpdateView):
    model = Contactos
    fields = ['nombre', 'email', 'birthdate', 'phone']
    success_url = reverse_lazy('crudContact_list')

class ContactDeleteView(generic.DeleteView):
    model = Contactos
    success_url = reverse_lazy('crudContact_list')