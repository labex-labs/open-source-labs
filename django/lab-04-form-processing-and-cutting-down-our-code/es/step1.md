# Escribe un formulario mínimo

Actualicemos la plantilla de detalle de encuesta (`polls/detail.html`) del último tutorial para que contenga un elemento HTML `<form>`:

```html+django
<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
<fieldset>
    <legend><h1>{{ question.question_text }}</h1></legend>
    {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}
    {% for choice in question.choice_set.all %}
        <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
        <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
    {% endfor %}
</fieldset>
<input type="submit" value="Vote">
</form>
```

Un repaso rápido:

- La plantilla anterior muestra un botón de radio para cada opción de pregunta. El `value` de cada botón de radio es el ID de la opción de pregunta asociada. El `name` de cada botón de radio es `"choice"`. Eso significa que, cuando alguien selecciona uno de los botones de radio y envía el formulario, enviará los datos POST `choice=#` donde \# es el ID de la opción seleccionada. Este es el concepto básico de los formularios HTML.
- Establecemos la `action` del formulario en `{% url 'polls:vote' question.id %}` y establecemos `method="post"`. Usar `method="post"` (en lugar de `method="get"`) es muy importante, porque la acción de enviar este formulario modificará los datos en el servidor. Siempre que crees un formulario que modifique los datos en el servidor, utiliza `method="post"`. Este consejo no es específico de Django; es una buena práctica de desarrollo web en general.
- `forloop.counter` indica cuántas veces la etiqueta `for` ha pasado por su bucle
- Dado que estamos creando un formulario POST (que puede tener el efecto de modificar datos), debemos preocuparnos por las falsificaciones de solicitud entre sitios (Cross Site Request Forgeries). Afortunadamente, no tienes que preocuparte demasiado, porque Django viene con un sistema útil para protegerse contra ello. En resumen, todos los formularios POST que apunten a URLs internas deben usar la etiqueta de plantilla `{% csrf_token %}<csrf_token>`.

Ahora, creemos una vista de Django que maneje los datos enviados y haga algo con ellos. Recuerda, en `**Creating the Public Interface Views**`, creamos una URLconf para la aplicación de encuestas que incluye esta línea:

```python
path("<int:question_id>/vote/", views.vote, name="vote"),
```

También creamos una implementación dummy de la función `vote()`. Vamos a crear una versión real. Agrega lo siguiente a `polls/views.py`:

```python
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from.models import Choice, Question


#...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Vuelva a mostrar el formulario de votación de la pregunta.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Siempre devuelve un HttpResponseRedirect después de manejar
        # correctamente los datos POST. Esto evita que los datos se envíen
        # dos veces si un usuario presiona el botón Atrás.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
```

Este código incluye algunas cosas que aún no hemos cubierto en este tutorial:

- `request.POST <django.http.HttpRequest.POST>` es un objeto similar a un diccionario que te permite acceder a los datos enviados por nombre de clave. En este caso, `request.POST['choice']` devuelve el ID de la opción seleccionada, como una cadena. Los valores de `request.POST <django.http.HttpRequest.POST>` siempre son cadenas.

  Tenga en cuenta que Django también proporciona `request.GET
<django.http.HttpRequest.GET>` para acceder a los datos GET de la misma manera, pero estamos usando explícitamente `request.POST
<django.http.HttpRequest.POST>` en nuestro código para asegurarnos de que los datos solo se modifiquen a través de una llamada POST.

- `request.POST['choice']` generará un `KeyError` si `choice` no se proporcionó en los datos POST. El código anterior verifica `KeyError` y vuelve a mostrar el formulario de pregunta con un mensaje de error si no se da `choice`.

- Después de incrementar el recuento de opciones, el código devuelve un `~django.http.HttpResponseRedirect` en lugar de un `~django.http.HttpResponse` normal. `~django.http.HttpResponseRedirect` toma un solo argumento: la URL a la que se redirigirá el usuario (vea el siguiente punto para ver cómo construimos la URL en este caso).

  Como señala el comentario de Python arriba, siempre deberías devolver un `~django.http.HttpResponseRedirect` después de manejar correctamente los datos POST. Este consejo no es específico de Django; es una buena práctica de desarrollo web en general.

- Estamos usando la función `~django.urls.reverse` en el constructor de `~django.http.HttpResponseRedirect` en este ejemplo. Esta función ayuda a evitar tener que codificar una URL en el función de vista. Se le da el nombre de la vista a la que queremos pasar el control y la parte variable del patrón de URL que apunta a esa vista. En este caso, usando la URLconf que configuramos en `**Creating the Public Interface Views**`, esta llamada a `~django.urls.reverse` devolverá una cadena como:

      "/polls/3/results/"

  donde el `3` es el valor de `question.id`. Esta URL redirigida luego llamará a la vista `'results'` para mostrar la página final.

Como se mencionó en `**Creating the Public Interface Views**`, `request` es un objeto `~django.http.HttpRequest`. Para obtener más información sobre los objetos `~django.http.HttpRequest`, consulte la `documentación de solicitud y
respuesta </ref/request-response>`.

Después de que alguien vota en una pregunta, la vista `vote()` redirige a la página de resultados de la pregunta. Escribamos esa vista:

```python
from django.shortcuts import get_object_or_404, render


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})
```

Esto es casi exactamente lo mismo que la vista `detail()` de **Creating the Public Interface Views**. La única diferencia es el nombre de la plantilla. Corregiremos esta redundancia más adelante.

Ahora, cree una plantilla `polls/results.html`:

```html+django
<h1>{{ question.question_text }}</h1>

<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
{% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote again?</a>
```

Ahora, vaya a `/polls/1/` en su navegador y vote en la pregunta. Debería ver una página de resultados que se actualiza cada vez que vota. Si envía el formulario sin haber elegido una opción, debería ver el mensaje de error.

```bash
cd ~/project/mysite
python manage.py runserver 0.0.0.0:8080
```

![Interfaz del formulario de votación de encuestas](../assets/20230908-10-37-07-p9ewKbe6.png)

**Nota:**

El código de nuestra vista `vote()` tiene un pequeño problema. Primero obtiene el objeto `selected_choice` de la base de datos, luego calcula el nuevo valor de `votes` y luego lo guarda de nuevo en la base de datos. Si dos usuarios de su sitio web intentan votar exactamente al mismo tiempo, esto puede salir mal: El mismo valor, digamos 42, se recuperará para `votes`. Luego, para ambos usuarios se calcula y guarda el nuevo valor de 43, pero 44 sería el valor esperado.

Esto se llama una _condición de carrera_. Si estás interesado, puedes leer `avoiding-race-conditions-using-f` para aprender cómo puedes resolver este problema.
