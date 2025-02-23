# Espacage des noms d'URL

Le projet de tutoriel n'a qu'une seule application, `polls`. Dans de vrais projets Django, il peut y avoir cinq, dix, vingt applications ou plus. Comment Django distingue-t-il les noms d'URL entre elles? Par exemple, l'application `polls` a une vue `detail`, et une application du même projet pour un blog pourrait également en avoir une. Comment peut-on s'assurer que Django sait quelle vue d'application créer pour une URL lorsqu'on utilise la balise de gabarit `{% url %}`?

La réponse est d'ajouter des espaces de noms à votre configuration d'URL. Dans le fichier `polls/urls.py`, allez-y et ajoutez un `app_name` pour définir l'espace de noms de l'application :

```python
from django.urls import path

from. import views

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

Maintenant, changez votre gabarit `polls/index.html` de :

```html+django
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

pour pointer vers la vue détaillée avec espace de noms :

```html+django
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```

![Exemple d'espacage des noms d'URL](../assets/20230908-09-58-22-qkl9l0DT.png)

Lorsque vous serez à l'aise pour écrire des vues, lisez **Traitement des formulaires et réduction de notre code** pour apprendre les bases sur le traitement des formulaires et les vues génériques.
