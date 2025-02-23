# Escribe vistas que realmente hagan algo

Cada vista es responsable de hacer una de dos cosas: devolver un objeto `~django.http.HttpResponse` que contenga el contenido de la página solicitada, o generar una excepción como `~django.http.Http404`. Lo demás depende de ti.

Tu vista puede leer registros de una base de datos, o no. Puede usar un sistema de plantillas como el de Django, o un sistema de plantillas de terceros para Python, o no. Puede generar un archivo PDF, emitir XML, crear un archivo ZIP en el vuelo, cualquier cosa que desees, usando cualquier biblioteca de Python que desees.

Todo lo que Django quiere es ese objeto `~django.http.HttpResponse`. O una excepción.

Por conveniencia, usemos la propia API de base de datos de Django, que cubrimos en el Tutorial 2. Aquí está un intento de una nueva vista `index()`, que muestra las últimas 5 preguntas de sondeo del sistema, separadas por comas, según la fecha de publicación:

Edite el archivo `polls/views.py` y cámbielo para que se vea así:

```python
from django.http import HttpResponse

from.models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


# Deje las demás vistas (detail, results, vote) sin cambios
```

Sin embargo, aquí hay un problema: el diseño de la página está codificado en duro en la vista. Si quieres cambiar la forma en que se ve la página, tendrás que editar este código de Python. Entonces, usemos el sistema de plantillas de Django para separar el diseño del Python creando una plantilla que la vista pueda usar.

Primero, cree un directorio llamado `templates` en su directorio `polls`. Django buscará plantillas ahí.

La configuración `TEMPLATES` de su proyecto describe cómo Django cargará y renderizará las plantillas. El archivo de configuración predeterminado configura un backend `DjangoTemplates` cuya opción `APP_DIRS <TEMPLATES-APP_DIRS>` está establecida en `True`. Por convención, `DjangoTemplates` busca un subdirectorio "templates" en cada una de las `INSTALLED_APPS`.

Dentro del directorio `templates` que acabas de crear, cree otro directorio llamado `polls`, y dentro de ese cree un archivo llamado `index.html`. En otras palabras, su plantilla debe estar en `polls/templates/polls/index.html`. Debido a cómo funciona el cargador de plantillas `app_directories` como se describe anteriormente, puede referirse a esta plantilla dentro de Django como `polls/index.html`.

## Espaciado de nombres de plantillas

Ahora _podríamos_ poder evitar poner nuestras plantillas directamente en `polls/templates` (en lugar de crear otro subdirectorio `polls`), pero en realidad sería una mala idea. Django elegirá la primera plantilla que encuentre cuyo nombre coincida, y si tuvieras una plantilla con el mismo nombre en una _diferente_ aplicación, Django no sería capaz de distinguir entre ellas.

Necesitamos poder apuntar a Django a la correcta, y la mejor manera de garantizar esto es mediante el _espaciado de nombres_. Es decir, al poner esas plantillas dentro de _otro_ directorio nombrado con el nombre de la aplicación misma.

Ponga el siguiente código en esa plantilla:

```html+django
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

Nota:

Para hacer el tutorial más corto, todos los ejemplos de plantilla usan HTML incompleto. En sus propios proyectos debe usar [documentos HTML completos](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started#anatomy_of_an_html_document).

Ahora actualicemos nuestra vista `index` en `polls/views.py` para usar la plantilla:

```python
from django.http import HttpResponse
from django.template import loader

from.models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```

Ese código carga la plantilla llamada `polls/index.html` y le pasa un contexto. El contexto es un diccionario que mapea los nombres de variables de plantilla a objetos de Python.

Ejecute el servidor nuevamente:

```bash
python manage.py runserver 0.0.0.0:8080
```

Cargue la página apuntando su navegador a "/polls/", y debería ver una lista con viñetas que contiene la pregunta "¿Qué pasa?" del Tutorial 2. El enlace apunta a la página de detalles de la pregunta.

![Django polls index page](../assets/20230908-09-37-26-QMKEbUhb.png)

## Un atajo: `~django.shortcuts.render`

Es un idioma muy común cargar una plantilla, llenar un contexto y devolver un objeto `~django.http.HttpResponse` con el resultado de la plantilla renderizada. Django proporciona un atajo. Aquí está la vista `index()` completa, reescrita:

```python
from django.shortcuts import render

from.models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
```

Tenga en cuenta que una vez que lo hemos hecho en todas estas vistas, ya no necesitamos importar `~django.template.loader` y `~django.http.HttpResponse` (deberá mantener `HttpResponse` si todavía tiene los métodos de esbozo para `detail`, `results` y `vote`).

La función `~django.shortcuts.render` toma el objeto de solicitud como su primer argumento, el nombre de una plantilla como su segundo argumento y un diccionario como su tercer argumento opcional. Devuelve un objeto `~django.http.HttpResponse` de la plantilla dada renderizada con el contexto dado.
