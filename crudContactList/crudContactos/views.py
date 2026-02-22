from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from crudContactos.models import Contactos

# Create your views here.
class ContactListView(generic.ListView):
    model = Contactos

    def get_queryset(self):
        return Contactos.objects.order_by('-favorito', 'nombre')


class ContactCreateView(generic.CreateView):
    model = Contactos # Redirect to home after successful creation
    fields = ['nombre', 'email', 'birthdate', 'phone', 'favorito', 'foto']
    success_url = reverse_lazy('crudContact_list')


class ContactUpdateView(generic.UpdateView):
    model = Contactos
    fields = ['nombre', 'email', 'birthdate', 'phone', 'favorito', 'foto']
    success_url = reverse_lazy('crudContact_list')

class ContactDeleteView(generic.DeleteView):
    model = Contactos
    success_url = reverse_lazy('crudContact_list')

def fijar_contacto(request, pk):
    contacto = Contactos.objects.filter(pk=pk).first()
    if contacto:
        contacto.favorito = not contacto.favorito
        contacto.save(update_fields=['favorito'])

    return redirect('crudContact_list')