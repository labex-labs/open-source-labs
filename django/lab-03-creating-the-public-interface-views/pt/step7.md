# Namespacing (Espaço de Nomes) de Nomes de URL

O projeto do tutorial tem apenas um app, `polls`. Em projetos Django reais, pode haver cinco, dez, vinte apps ou mais. Como o Django diferencia os nomes de URL entre eles? Por exemplo, o app `polls` tem uma view `detail`, e o mesmo pode acontecer com um app no mesmo projeto que é para um blog. Como se faz para que o Django saiba qual view de app criar para uma URL ao usar a tag de template `{% url %}`?

A resposta é adicionar namespaces (espaços de nomes) ao seu URLconf. No arquivo `polls/urls.py`, adicione um `app_name` para definir o namespace da aplicação:

```python
from django.urls import path

from . import views

app_name = "polls"
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

Agora, altere seu template `polls/index.html` de:

```html+django
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

para apontar para a view de detalhes com namespace:

```html+django
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```

![URL namespacing example](../assets/20230908-09-58-22-qkl9l0DT.png)

Quando você estiver confortável com a escrita de views, leia **Processamento de Formulários e Reduzindo Nosso Código** para aprender o básico sobre processamento de formulários e views genéricas.
