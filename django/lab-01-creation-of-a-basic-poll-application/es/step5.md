# Escribe tu primera vista

Vamos a escribir la primera vista. Abre el archivo `polls/views.py` y pon el siguiente código de Python en él:

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

Esta es la vista más simple posible en Django. Para llamar a la vista, necesitamos mapearla a una URL, y para esto necesitamos una configuración de URL (URLconf).

Para crear una URLconf en el directorio de polls, crea un archivo llamado `urls.py`. Tu directorio de aplicación ahora debería verse así:

```plaintext
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py
```

En el archivo `polls/urls.py`, incluye el siguiente código:

```python
from django.urls import path

from. import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

El siguiente paso es apuntar la URLconf principal al módulo `polls.urls`. En `mysite/urls.py`, agrega una importación para `django.urls.include` e inserta un `~django.urls.include` en la lista `urlpatterns`, de modo que tengas:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```

La función `~django.urls.include` permite referenciar otras configuraciones de URL. Siempre que Django encuentra `~django.urls.include`, corta cualquier parte de la URL que haya coincidido hasta ese punto y envía el resto de la cadena a la configuración de URL incluida para su procesamiento adicional.

La idea detrás de `~django.urls.include` es facilitar la inserción y reproducción de URLs. Dado que las encuestas están en su propia configuración de URL (`polls/urls.py`), pueden ubicarse bajo "/polls/", o bajo "/fun_polls/", o bajo "/content/polls/", o cualquier otro directorio raíz, y la aplicación todavía funcionará.

> Cuando usar `~django.urls.include()`
> Siempre debes usar `include()` cuando incluyas otros patrones de URL. `admin.site.urls` es la única excepción a esto.

Ahora has conectado una vista `index` a la URLconf. Verifica que está funcionando con el siguiente comando:

```bash
python manage.py runserver 0.0.0.0:8080
```

Ve a <http://<url>/polls/> en tu navegador, y deberías ver el texto "_Hello, world. You're at the polls index._", que definiste en la vista `index`.

![Estructura de la URLconf de Django](../assets/20230907-13-51-48-aOKKfCBX.png)

La función `~django.urls.path` se le pasa cuatro argumentos, dos obligatorios: `route` y `view`, y dos opcionales: `kwargs` y `name`. En este momento, vale la pena revisar para qué sirven estos argumentos.

## Argumento de `~django.urls.path`: `route`

`route` es una cadena que contiene un patrón de URL. Al procesar una solicitud, Django comienza con el primer patrón en `urlpatterns` y recorre la lista, comparando la URL solicitada con cada patrón hasta encontrar uno que coincida.

Los patrones no buscan parámetros GET y POST, ni el nombre de dominio. Por ejemplo, en una solicitud a `https://www.example.com/myapp/`, la URLconf buscará `myapp/`. En una solicitud a `https://www.example.com/myapp/?page=3`, la URLconf también buscará `myapp/`.

## Argumento de `~django.urls.path`: `view`

Cuando Django encuentra un patrón que coincide, llama a la función de vista especificada con un objeto `~django.http.HttpRequest` como primer argumento y cualquier valor "capturado" de la ruta como argumentos de palabras clave. Daremos un ejemplo de esto más adelante.

## Argumento de `~django.urls.path`: `kwargs`

Se pueden pasar argumentos de palabras clave arbitrarios en un diccionario a la vista destino. No vamos a usar esta característica de Django en el tutorial.

## Argumento de `~django.urls.path`: `name`

Dar un nombre a tu URL te permite referirte a ella de manera inambigua desde otros lugares en Django, especialmente desde dentro de plantillas. Esta característica poderosa te permite hacer cambios globales en los patrones de URL de tu proyecto mientras solo modificas un solo archivo.
