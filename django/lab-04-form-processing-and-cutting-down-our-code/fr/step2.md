# Utiliser les vues génériques : moins de code est mieux

La vue `detail()` (issue de `**Creating the Public Interface Views**`) et la vue `results()` sont très courtes - et, comme mentionné ci-dessus, redondantes. La vue `index()`, qui affiche une liste de sondages, est similaire.

Ces vues représentent un cas courant du développement web de base : récupérer des données depuis la base de données selon un paramètre passé dans l'URL, charger un modèle et renvoyer le modèle rendu. Comme cela est très courant, Django propose un raccourci, appelé système de "vues génériques".

Les vues génériques abstraient les modèles communs au point où vous n'avez même pas besoin d'écrire du code Python pour écrire une application.

Convertissons notre application de sondage pour utiliser le système de vues génériques, afin que nous puissions supprimer un certain nombre de notre propre code. Nous devrons prendre quelques étapes pour effectuer la conversion. Nous allons :

1. Convertir la configuration d'URL.
2. Supprimer certaines des anciennes vues inutiles.
3. Introduire de nouvelles vues basées sur les vues génériques de Django.

Lisez ci-dessous pour plus de détails.

> Pourquoi le remaniement du code?

Généralement, lorsqu'on écrit une application Django, on évaluera si les vues génériques sont appropriées pour votre problème, et on les utilisera dès le départ, plutôt que de refactoriser votre code au milieu du chemin. Mais ce tutoriel a intentionnellement mis l'accent sur l'écriture des vues "de manière difficile" jusqu'à présent, pour se concentrer sur les concepts clés.

Vous devriez connaître les mathématiques de base avant de commencer à utiliser une calculatrice.

## Modifier la configuration d'URL

Tout d'abord, ouvrez la configuration d'URL `polls/urls.py` et modifiez-la comme suit :

```python
from django.urls import path

from. import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

Notez que le nom du motif correspondant dans les chaînes de caractères de chemin des deuxième et troisième motifs est passé de `<question_id>` à `<pk>`.

## Modifier les vues

Ensuite, nous allons supprimer nos anciennes vues `index`, `detail` et `results` et utiliser les vues génériques de Django à la place. Pour ce faire, ouvrez le fichier `polls/views.py` et modifiez-le comme suit :

```python
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from.models import Choice, Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Retourne les cinq dernières questions publiées."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
  ...  # identique à ci-dessus, pas de modifications nécessaires.
```

Nous utilisons ici deux vues génériques : `~django.views.generic.list.ListView` et `~django.views.generic.detail.DetailView`. respectivement, ces deux vues abstraient les concepts de "afficher une liste d'objets" et "afficher une page de détails pour un type particulier d'objet".

- Chaque vue générique doit savoir quel modèle elle va agir sur. Cela est fourni en utilisant l'attribut `model`.
- La vue générique `~django.views.generic.detail.DetailView` attend que la valeur de la clé primaire capturée depuis l'URL soit appelée `"pk"`, donc nous avons changé `question_id` en `pk` pour les vues génériques.

Par défaut, la vue générique `~django.views.generic.detail.DetailView` utilise un modèle appelé `<nom de l'application>/<nom du modèle>_detail.html`. Dans notre cas, il utiliserait le modèle `"polls/question_detail.html"`. L'attribut `template_name` est utilisé pour dire à Django d'utiliser un nom de modèle spécifique au lieu du nom de modèle par défaut autogénéré. Nous spécifions également le `template_name` pour la vue de liste `results` - cela garantit que la vue de résultats et la vue de détails ont une apparence différente lorsqu'elles sont rendues, même si elles sont toutes deux une `~django.views.generic.detail.DetailView` en coulisse.

De manière similaire, la vue générique `~django.views.generic.list.ListView` utilise un modèle par défaut appelé `<nom de l'application>/<nom du modèle>_list.html` ; nous utilisons `template_name` pour dire à `~django.views.generic.list.ListView` d'utiliser notre modèle existant `"polls/index.html"`.

Dans les parties précédentes du tutoriel, les modèles ont été fournis avec un contexte qui contient les variables de contexte `question` et `latest_question_list`. Pour `DetailView`, la variable `question` est fournie automatiquement - puisque nous utilisons un modèle Django (`Question`), Django est capable de déterminer un nom approprié pour la variable de contexte. Cependant, pour `ListView`, la variable de contexte automatiquement générée est `question_list`. Pour la surcharger, nous fournissons l'attribut `context_object_name`, en spécifiant que nous voulons utiliser `latest_question_list` à la place. En tant qu'approche alternative, vous pourriez modifier vos modèles pour correspondre aux nouvelles variables de contexte par défaut - mais il est beaucoup plus facile de dire à Django d'utiliser la variable que vous voulez.

Exécutez le serveur et utilisez votre nouvelle application de sondage basée sur les vues génériques.
