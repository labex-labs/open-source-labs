# Espaciado de nombres de URL

El proyecto del tutorial solo tiene una aplicación, `polls`. En los proyectos reales de Django, pueden haber cinco, diez, veinte aplicaciones o más. ¿Cómo distingue Django los nombres de URL entre ellas? Por ejemplo, la aplicación `polls` tiene una vista `detail`, y también podría haber una aplicación en el mismo proyecto que es para un blog. ¿Cómo se hace para que Django sepa qué vista de aplicación crear para una URL cuando se utiliza la etiqueta de plantilla `{% url %}`?

La respuesta es agregar espacios de nombres a su URLconf. En el archivo `polls/urls.py`, agregue un `app_name` para establecer el espacio de nombres de la aplicación:

```python
from django.urls import path

from. import views

app_name = "polls"
urlpatterns = [
    # ej: /polls/
    path("", views.index, name="index"),
    # ej: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ej: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ej: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

Ahora cambie su plantilla `polls/index.html` de:

```html+django
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

para apuntar a la vista de detalles con espaciado de nombres:

```html+django
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```

![URL namespacing example](../assets/20230908-09-58-22-qkl9l0DT.png)

Cuando esté cómodo escribiendo vistas, lea **Procesamiento de formularios y reducción de nuestro código** para aprender los conceptos básicos sobre el procesamiento de formularios y vistas genéricas.
