from django.urls import path
from .views import inicio,archivo_2,archivo_3,formulario,API,crear,eliminar,modificar,otra,registrar

urlpatterns=[ 
    path('', inicio, name="inicio"),
    path('archivo_2/',archivo_2, name="archivo_2"),
    path('archivo_3/',archivo_3, name="archivo_3"),
    path('formulario/',formulario, name="formulario"),
    path('API/',API, name="API"),
    path('otra/',otra,name="otra"),
    path('crear/',crear,name="crear"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('modificar/<id>', modificar, name="modificar"),
    path('registrar/',registrar,name="registrar"),
]