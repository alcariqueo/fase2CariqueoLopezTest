from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usuario/<int:pk>', views.UsuarioDetailView.as_view(), name='usuario-detail'),
    path('partidos/',views.PartidoListView.as_view(), name='partidos'),
    path('partidos/<int:pk>', views.PartidoDetailView.as_view(), name='partido-detail'),
]

urlpatterns+=[
    path('usuario/create/', views.UsuarioCreate.as_view(), name='usuario_create'),
    path('usuario/<int:pk>/update/', views.UsuarioUpdate.as_view(), name='usuario_update'),
    path('usuario/<int:pk>/delete/', views.UsuarioDelete.as_view(), name='usuario_delete'),
    

]
