# Utiliza vistas genéricas: menos código es mejor

Las vistas `detail()` (de `**Creating the Public Interface Views**`) y `results()` son muy cortas y, como se mencionó anteriormente, redundantes. La vista `index()`, que muestra una lista de encuestas, es similar.

Estas vistas representan un caso común en el desarrollo web básico: obtener datos de la base de datos de acuerdo con un parámetro pasado en la URL, cargar una plantilla y devolver la plantilla renderizada. Debido a que esto es muy común, Django proporciona un atajo llamado el sistema de "vistas genéricas".

Las vistas genéricas abstraen patrones comunes al punto de que ni siquiera necesitas escribir código de Python para escribir una aplicación.

Convertamos nuestra aplicación de encuestas para usar el sistema de vistas genéricas, para que podamos eliminar un montón de nuestro propio código. Tendremos que dar algunos pasos para hacer la conversión. Vamos a:

1. Convertir la URLconf.
2. Eliminar algunas de las viejas vistas innecesarias.
3. Introducir nuevas vistas basadas en las vistas genéricas de Django.

Sigue leyendo para obtener detalles.

> ¿Por qué el reordenamiento de código?

En general, al escribir una aplicación de Django, evaluarás si las vistas genéricas son adecuadas para tu problema y las usarás desde el principio, en lugar de refactorizar tu código en mitad del proceso. Pero este tutorial intencionalmente se ha centrado en escribir las vistas "de manera difícil" hasta ahora, para centrarse en los conceptos básicos.

Debes conocer las matemáticas básicas antes de comenzar a usar una calculadora.

## Modifica la URLconf

Primero, abre la URLconf `polls/urls.py` y cámbiala de la siguiente manera:

```python
from django.urls import path

from. import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

Observa que el nombre del patrón coincidente en las cadenas de ruta de los segundos y tercer patrones ha cambiado de `<question_id>` a `<pk>`.

## Modifica las vistas

A continuación, vamos a eliminar nuestras viejas vistas `index`, `detail` y `results` y usar en su lugar las vistas genéricas de Django. Para hacer eso, abre el archivo `polls/views.py` y cámbialo de la siguiente manera:

```python
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from.models import Choice, Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Devuelve las últimas cinco preguntas publicadas."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
  ...  # es el mismo que arriba, no se necesitan cambios.
```

Estamos usando dos vistas genéricas aquí: `~django.views.generic.list.ListView` y `~django.views.generic.detail.DetailView`. Respectivamente, esas dos vistas abstraen los conceptos de "mostrar una lista de objetos" y "mostrar una página de detalles para un tipo particular de objeto".

- Cada vista genérica necesita saber qué modelo sobre el que actuará. Esto se proporciona usando el atributo `model`.
- La vista genérica `~django.views.generic.detail.DetailView` espera que el valor de la clave primaria capturado de la URL se llame `"pk"`, por lo que hemos cambiado `question_id` a `pk` para las vistas genéricas.

Por defecto, la vista genérica `~django.views.generic.detail.DetailView` utiliza una plantilla llamada `<nombre de la aplicación>/<nombre del modelo>_detail.html`. En nuestro caso, usaría la plantilla `"polls/question_detail.html"`. El atributo `template_name` se utiliza para decirle a Django que use un nombre de plantilla específico en lugar del nombre de plantilla predeterminado automático. También especificamos el `template_name` para la vista de lista de `results`; esto garantiza que la vista de resultados y la vista de detalles tengan una apariencia diferente cuando se renderizan, aunque en realidad ambas son una `~django.views.generic.detail.DetailView` detrás de escena.

Del mismo modo, la vista genérica `~django.views.generic.list.ListView` utiliza una plantilla predeterminada llamada `<nombre de la aplicación>/<nombre del modelo>_list.html`; usamos `template_name` para decirle a `~django.views.generic.list.ListView` que use nuestra plantilla existente `"polls/index.html"`.

En partes anteriores del tutorial, las plantillas se han proporcionado con un contexto que contiene las variables de contexto `question` y `latest_question_list`. Para `DetailView`, la variable `question` se proporciona automáticamente, ya que estamos usando un modelo de Django (`Question`), Django es capaz de determinar un nombre adecuado para la variable de contexto. Sin embargo, para ListView, la variable de contexto generada automáticamente es `question_list`. Para anular esto, proporcionamos el atributo `context_object_name`, especificando que queremos usar `latest_question_list` en lugar de eso. Como enfoque alternativo, podrías cambiar tus plantillas para que coincidan con las nuevas variables de contexto predeterminadas, pero es mucho más fácil decirle a Django que use la variable que quieres.

Ejecuta el servidor y utiliza tu nueva aplicación de encuestas basada en vistas genéricas.
