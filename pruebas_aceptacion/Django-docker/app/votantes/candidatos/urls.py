from django.urls import path, include
from candidatos import views
from .views import NuevoVoto, ListaResultados
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.ListaCandidatos.as_view(), name = 'lista_cantidatos'),
    path('resultados', ListaResultados, name = 'resultados'),
    path('votaciones/<int:candidato_id>/', NuevoVoto, name = 'nuevo_voto'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
