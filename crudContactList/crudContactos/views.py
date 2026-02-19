from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.http import require_POST
from django.db.models import Max
from crudContactos.models import Contactos

# Create your views here.
class ContactListView(generic.ListView):
    model = Contactos

    def get_queryset(self):
        return Contactos.objects.order_by('-fijado', 'fijado_orden', 'nombre')


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

def fijar_contacto(request, pk):
    contacto = Contactos.objects.filter(pk=pk).first()
    if contacto:
        if contacto.fijado:
            contacto.fijado = False
            contacto.fijado_orden = None
        else:
            ultimo_orden = Contactos.objects.filter(fijado=True).aggregate(Max('fijado_orden'))['fijado_orden__max'] or 0
            contacto.fijado = True
            contacto.fijado_orden = ultimo_orden + 1
        contacto.save(update_fields=['fijado', 'fijado_orden'])

    return redirect('crudContact_list')