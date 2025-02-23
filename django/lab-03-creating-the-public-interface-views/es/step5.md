# Utiliza el sistema de plantillas

Volvamos a la vista `detail()` de nuestra aplicación de sondeo. Dada la variable de contexto `question`, así podría verse la plantilla `polls/detail.html`:

```html+django
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```

El sistema de plantillas utiliza la sintaxis de búsqueda por puntos para acceder a los atributos de las variables. En el ejemplo de `{{ question.question_text }}`, primero Django realiza una búsqueda en el diccionario del objeto `question`. Si falla, intenta una búsqueda de atributo, lo que funciona en este caso. Si la búsqueda de atributo hubiera fallado, habría intentado una búsqueda por índice de lista.

La llamada a métodos se produce en el bucle `{% for %}<for>`: `question.choice_set.all` se interpreta como el código de Python `question.choice_set.all()`, que devuelve un iterable de objetos `Choice` y es adecuado para utilizarse en la etiqueta `{% for %}<for>`.
