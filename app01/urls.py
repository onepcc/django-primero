from django.urls import path     
from . import views
urlpatterns = [
    path('', views.root),
    path('blogs',views.index),
    path('blogs/new', views.new),
    path('blogs/create', views.create),
    path('blogs/<int:number>', views.show),
    # path('blogs/<str:nombre>', views.show),
    path('blogs/<int:number>/edit', views.edit),
    path('blogs/<int:number>/delete', views.destroy),
    path('blogs/json', views.json_test)
    
    
]

#lo que va despues del views es el metodo

#  Crea un nuevo proyecto con una sola aplicación, ok

#  / - redirige a la ruta "/blogs" con el método llamado "root", ok

#  /blogs - muestra el string "placeholder para luego mostrar una lista de todos los blogs" con un método llamado "index"

#  /blogs/new - muestra el string "placeholder para mostrar un nuevo formulario para crear un nuevo blog" con un método llamado "new"

#  /blogs/create - redirige a la ruta "/" con un método llamado "create"

#  /blogs/< number > - muestra el string "placeholder para mostrar el blog numero: {number}" con un método llamado "show" (ej. localhost:8000/blogs/15 debería mostrar el mensaje: 'placeholder para mostrar el blog numero 15')

#  /blogs/< number >/edit - muestra el string "placeholder para editar el blog {number}" con un método llamado "edit"

#  /blogs/< number >/delete - redirige a la ruta "/blogs" con el método llamado "destroy"

#  (**Bonus**) /blogs/json - regresa una JsonResponse con un titulo y que contenga llaves.