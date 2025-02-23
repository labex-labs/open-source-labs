# Eliminando URLs codificadas en duro en las plantillas

Recuerde, cuando escribimos el enlace a una pregunta en la plantilla `polls/index.html`, el enlace estaba parcialmente codificado en duro de la siguiente manera:

```html+django
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
```

El problema de este enfoque codificado en duro y fuertemente acoplado es que se vuelve difícil cambiar las URLs en proyectos con muchas plantillas. Sin embargo, dado que definiste el argumento `name` en las funciones `~django.urls.path` del módulo `polls.urls`, puedes eliminar la dependencia de las rutas de URL específicas definidas en tus configuraciones de URL mediante la etiqueta de plantilla `{% url %}`:

```html+django
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

La forma en que funciona es buscando la definición de URL como se especifica en el módulo `polls.urls`. Puedes ver exactamente dónde se define el nombre de URL de 'detail' a continuación:

```python
# el valor 'name' como se llama por la etiqueta de plantilla {% url %}
path("<int:question_id>/", views.detail, name="detail"),
```

Si quieres cambiar la URL de la vista de detalles de los sondeos a algo diferente, quizás a algo como `polls/specifics/12/` en lugar de hacerlo en la plantilla (o plantillas), lo cambiarías en `polls/urls.py`:

> No es necesario cambiar la plantilla en absoluto.

```python
# se agregó la palabra'specifics'
path("specifics/<int:question_id>/", views.detail, name="detail"),
```
