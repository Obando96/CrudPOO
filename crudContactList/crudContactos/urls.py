from django.urls import path
from crudContactos import views
urlpatterns = [
    path('', views.ContactListView.as_view(), name='crudContact_list'),
    path('<int:pk>/fijar/', views.fijar_contacto, name='crudContact_fix'),
    path('new/', views.ContactCreateView.as_view(), name='crudContact_new'),
    path('<int:pk>/edit/', views.ContactUpdateView.as_view(), name='crudContact_edit'),
    path('<int:pk>/delete/', views.ContactDeleteView.as_view(), name='crudContact_delete'),
]