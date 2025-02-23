# Écrire plus de vues

Maintenant, ajoutons quelques vues supplémentaires à `polls/views.py`. Ces vues sont légèrement différentes, car elles prennent un argument :

```python
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

Reliez ces nouvelles vues au module `polls.urls` en ajoutant les appels suivants à `~django.urls.path` :

Modifiez le fichier `polls/urls.py` et ajoutez les lignes suivantes :

```python
from django.urls import path

from. import views

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

Maintenant, exécutez le serveur à nouveau :

```bash
cd ~/project/mysite
python manage.py runserver 0.0.0.0:8080
```

Accédez à l'onglet **Web 8080**, à `/polls/34/`. Cela exécutera la méthode `detail()` et affichera l'ID que vous fournissez dans l'URL. Essayez également `/polls/34/results/` et `/polls/34/vote/` - ces derniers afficheront les pages de résultats et de vote de remplacement.

![Django URL routing diagram](../assets/20230908-09-30-06-2n54ROPe.png)

Lorsque quelqu'un demande une page de votre site web - disons, `/polls/34/`, Django chargera le module Python `mysite.urls` car il est indiqué par la configuration `ROOT_URLCONF`. Il trouve la variable nommée `urlpatterns` et parcourt les motifs dans l'ordre. Après avoir trouvé la correspondance à `'polls/'`, il enlève le texte correspondant (`"polls/"`) et envoie le texte restant - `"34/"` - au fichier de configuration d'URL `'polls.urls'` pour traitement supplémentaire. Là, il correspond à `'<int:question_id>/'`, ce qui résulte dans un appel à la vue `detail()` comme suit :

```python
detail(request=<HttpRequest object>, question_id=34)
```

La partie `question_id=34` vient de `<int:question_id>`. En utilisant des crochets, on "captue" une partie de l'URL et on l'envoie en tant qu'argument clé-valeur à la fonction de vue. La partie `question_id` de la chaîne définit le nom qui sera utilisé pour identifier le motif correspondant, et la partie `int` est un convertisseur qui détermine quels motifs devraient correspondre à cette partie du chemin d'URL. Le deux-points (`:`) sépare le convertisseur et le nom du motif.
