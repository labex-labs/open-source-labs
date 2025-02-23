# Escribiendo más vistas

Ahora agreguemos algunas más vistas a `polls/views.py`. Estas vistas son un poco diferentes, porque toman un argumento:

```python
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

Conecte estas nuevas vistas al módulo `polls.urls` agregando las siguientes llamadas a `~django.urls.path`:

Edite el archivo `polls/urls.py` y agregue las siguientes líneas:

```python
from django.urls import path

from. import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

Ahora, ejecute el servidor nuevamente:

```bash
cd ~/project/mysite
python manage.py runserver 0.0.0.0:8080
```

Vaya a la pestaña **Web 8080**, en `/polls/34/`. Ejecutará el método `detail()` y mostrará el ID que proporcione en la URL. Pruebe también `/polls/34/results/` y `/polls/34/vote/`; estos mostrarán las páginas de resultados y de votación con marcadores de posición.

![Django URL routing diagram](../assets/20230908-09-30-06-2n54ROPe.png)

Cuando alguien solicita una página de su sitio web, digamos, `/polls/34/`, Django cargará el módulo de Python `mysite.urls` porque está apuntado por la configuración `ROOT_URLCONF`. Encuentra la variable llamada `urlpatterns` y recorre los patrones en orden. Después de encontrar la coincidencia en `'polls/'`, quita el texto coincidente (`"polls/"`) y envía el texto restante, `"34/"`, al URLconf de `'polls.urls'` para su procesamiento adicional. Allí coincide con `'<int:question_id>/'`, lo que resulta en una llamada a la vista `detail()` de la siguiente manera:

```python
detail(request=<HttpRequest object>, question_id=34)
```

La parte `question_id=34` proviene de `<int:question_id>`. Usando corchetes angulares, "captura" una parte de la URL y la envía como un argumento de palabras clave a la función de vista. La parte `question_id` de la cadena define el nombre que se usará para identificar el patrón coincidente, y la parte `int` es un convertidor que determina qué patrones deben coincidir con esta parte de la ruta de URL. El dos puntos (`:`) separa el convertidor y el nombre del patrón.
