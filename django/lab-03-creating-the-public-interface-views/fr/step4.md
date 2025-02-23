# Lèvement d'une erreur 404

Maintenant, abordons la vue de détail des questions - la page qui affiche le texte de la question pour un sondage donné. Voici la vue :

```python
from django.http import Http404
from django.shortcuts import render

from.models import Question


#...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})
```

Le nouveau concept ici : La vue lève l'exception `~django.http.Http404` si une question avec l'ID demandé n'existe pas.

Nous discuterons de ce que vous pourriez mettre dans le gabarit `polls/detail.html` un peu plus tard, mais si vous voulez rapidement faire fonctionner l'exemple ci-dessus, un fichier contenant seulement :

```html+django
{{ question }}
```

vous permettra de commencer pour l'instant.

## Un raccourci : `~django.shortcuts.get_object_or_404`

Il est très courant d'utiliser `~django.db.models.query.QuerySet.get` et de lever `~django.http.Http404` si l'objet n'existe pas. Django propose un raccourci. Voici la vue `detail()`, réécrite :

```python
from django.shortcuts import get_object_or_404, render

from.models import Question


#...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
```

La fonction `~django.shortcuts.get_object_or_404` prend un modèle Django comme premier argument et un nombre arbitraire d'arguments clés, qu'elle passe à la fonction `~django.db.models.query.QuerySet.get` du gestionnaire du modèle. Elle lève `~django.http.Http404` si l'objet n'existe pas.

Pourquoi utilisons-nous une fonction d'aide `~django.shortcuts.get_object_or_404` au lieu de capturer automatiquement les exceptions `~django.core.exceptions.ObjectDoesNotExist` à un niveau supérieur, ou de faire en sorte que l'API du modèle lève `~django.http.Http404` au lieu de `~django.core.exceptions.ObjectDoesNotExist`?

Parce que cela couplerait la couche modèle à la couche vue. L'un des objectifs de conception principaux de Django est de maintenir un faible couplage. Un certain couplage contrôlé est introduit dans le module `django.shortcuts`.

Il existe également une fonction `~django.shortcuts.get_list_or_404`, qui fonctionne comme `~django.shortcuts.get_object_or_404` - sauf qu'elle utilise `~django.db.models.query.QuerySet.filter` au lieu de `~django.db.models.query.QuerySet.get`. Elle lève `~django.http.Http404` si la liste est vide.
