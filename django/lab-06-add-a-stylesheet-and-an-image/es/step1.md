# Personaliza el aspecto de tu _app_

Primero, crea un directorio llamado `static` en tu directorio `polls`. Django buscará archivos estáticos allí, de manera similar a cómo Django encuentra templates dentro de `polls/templates/`.

La configuración `STATICFILES_FINDERS` de Django contiene una lista de buscadores que saben cómo descubrir archivos estáticos a partir de diferentes fuentes. Uno de los valores predeterminados es `AppDirectoriesFinder` que busca un subdirectorio "static" en cada una de las `INSTALLED_APPS`, como el que creamos recientemente en `polls`. El sitio de administración utiliza la misma estructura de directorios para sus archivos estáticos.

Dentro del directorio `static` que acabas de crear, crea otro directorio llamado `polls` y dentro de ese crea un archivo llamado `style.css`. En otras palabras, tu hoja de estilos debe estar en `polls/static/polls/style.css`. Debido a cómo funciona el buscador de archivos estáticos `AppDirectoriesFinder`, puedes referirte a este archivo estático en Django como `polls/style.css`, de manera similar a cómo referenciar la ruta para templates.

## Espaciado de nombres de archivos estáticos

Al igual que con los templates, _podríamos_ poder evitar poner nuestros archivos estáticos directamente en `polls/static` (en lugar de crear otro subdirectorio `polls`), pero en realidad sería una mala idea. Django elegirá el primer archivo estático que encuentre cuyo nombre coincida, y si tuvieras un archivo estático con el mismo nombre en una _diferente_ aplicación, Django no sería capaz de distinguir entre ellos. Necesitamos poder indicar a Django cuál es el correcto, y la mejor manera de garantizar esto es mediante el _espaciado de nombres_. Es decir, al poner esos archivos estáticos dentro de _otro_ directorio nombrado con el nombre de la aplicación misma.

Pon el siguiente código en esa hoja de estilos (`polls/static/polls/style.css`):

```css
li a {
  color: green;
}
```

Luego, agrega lo siguiente al principio de `polls/templates/polls/index.html`:

```html+django
{% load static %}

<link rel="stylesheet" href="{% static 'polls/style.css' %}">
```

La etiqueta de plantilla `{% static %}` genera la URL absoluta de los archivos estáticos.

Eso es todo lo que necesitas hacer para el desarrollo.

Inicia el servidor (o reinícialo si ya está en ejecución):

```bash
python manage.py runserver 0.0.0.0:8080
```

Recarga la pestaña **Web 8080** y deberías ver que los enlaces de las preguntas son de color verde (¡estilo Django!), lo que significa que tu hoja de estilos se cargó correctamente.

![green question links example](../assets/20230908-15-29-11-ztyI1umP.png)
