# Lanzando un error 404

Ahora, abordemos la vista de detalles de la pregunta, la página que muestra el texto de la pregunta para un sondeo dado. Aquí está la vista:

```python
from django.http import Http404
from django.shortcuts import render

from.models import Question


#...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})
```

El nuevo concepto aquí: La vista lanza la excepción `~django.http.Http404` si no existe una pregunta con el ID solicitado.

Vamos a discutir un poco más adelante qué podrías poner en esa plantilla `polls/detail.html`, pero si quieres que el ejemplo anterior funcione rápidamente, un archivo que contenga solo:

```html+django
{{ question }}
```

te ayudará a empezar por ahora.

## Un atajo: `~django.shortcuts.get_object_or_404`

Es un idioma muy común usar `~django.db.models.query.QuerySet.get` y lanzar `~django.http.Http404` si el objeto no existe. Django proporciona un atajo. Aquí está la vista `detail()`, reescrita:

```python
from django.shortcuts import get_object_or_404, render

from.models import Question


#...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
```

La función `~django.shortcuts.get_object_or_404` toma un modelo de Django como su primer argumento y un número arbitrario de argumentos de palabras clave, que pasa a la función `~django.db.models.query.QuerySet.get` del administrador del modelo. Lanza `~django.http.Http404` si el objeto no existe.

¿Por qué usamos una función auxiliar `~django.shortcuts.get_object_or_404` en lugar de capturar automáticamente las excepciones `~django.core.exceptions.ObjectDoesNotExist` en un nivel superior, o hacer que la API del modelo lance `~django.http.Http404` en lugar de `~django.core.exceptions.ObjectDoesNotExist`?

Porque eso uniría la capa del modelo a la capa de la vista. Uno de los objetivos de diseño principales de Django es mantener un acoplamiento débil. Un poco de acoplamiento controlado se introduce en el módulo `django.shortcuts`.

También hay una función `~django.shortcuts.get_list_or_404`, que funciona de la misma manera que `~django.shortcuts.get_object_or_404`, excepto que utiliza `~django.db.models.query.QuerySet.filter` en lugar de `~django.db.models.query.QuerySet.get`. Lanza `~django.http.Http404` si la lista está vacía.
