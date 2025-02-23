# Suppression d'URLs codées en dur dans les gabarits

Souvenez-vous, lorsque nous avons écrit le lien vers une question dans le gabarit `polls/index.html`, le lien était partiellement codé en dur comme ceci :

```html+django
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
```

Le problème de cette approche codée en dur et fortement couplée est qu'il devient difficile de changer les URLs dans des projets avec beaucoup de gabarits. Cependant, puisque vous avez défini l'argument `name` dans les fonctions `~django.urls.path` du module `polls.urls`, vous pouvez éliminer la dépendance sur les chemins d'URL spécifiques définis dans vos configurations d'URL en utilisant la balise de gabarit `{% url %}` :

```html+django
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

Le fonctionnement de cela consiste à rechercher la définition d'URL telle que spécifiée dans le module `polls.urls`. Vous pouvez voir exactement où le nom d'URL 'detail' est défini ci-dessous :

```python
# la valeur 'name' appelée par la balise de gabarit {% url %}
path("<int:question_id>/", views.detail, name="detail"),
```

Si vous voulez changer l'URL de la vue de détail des sondages en quelque chose d'autre, peut-être en `polls/specifics/12/` au lieu de le faire dans le gabarit (ou les gabarits), vous le changeriez dans `polls/urls.py` :

> Vous n'avez pas besoin de changer le gabarit du tout.

```python
# ajout du mot'specifics'
path("specifics/<int:question_id>/", views.detail, name="detail"),
```
