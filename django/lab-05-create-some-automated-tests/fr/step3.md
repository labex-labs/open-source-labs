# Écrire notre premier test

## Nous identifions un bogue

Heureusement, il y a un petit bogue dans l'application `polls` que nous pouvons corriger immédiatement : la méthode `Question.was_published_recently()` renvoie `True` si la `Question` a été publiée dans le dernier jour (ce qui est correct), mais également si le champ `pub_date` de la `Question` est dans l'avenir (ce qui n'est certainement pas le cas).

Confirmez le bogue en utilisant le `shell` pour vérifier la méthode sur une question dont la date est dans l'avenir :

```bash
cd ~/project/mysite
python manage.py shell
```

```python
>>> import datetime
>>> from django.utils import timezone
>>> from polls.models import Question
>>> # créez une instance de Question avec pub_date dans 30 jours
>>> future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
>>> # a-t-elle été publiée récemment?
>>> future_question.was_published_recently()
True
```

Puisque les choses de l'avenir ne sont pas "récentes", c'est clairement faux.

## Créer un test pour démasquer le bogue

Ce que nous venons de faire dans le `shell` pour tester le problème est exactement ce que nous pouvons faire dans un test automatisé, donc transformons cela en un test automatisé.

Un emplacement conventionnel pour les tests d'une application est dans le fichier `tests.py` de l'application ; le système de test trouvera automatiquement les tests dans tout fichier dont le nom commence par `test`.

Placez le code suivant dans le fichier `tests.py` de l'application `polls` :

```python
import datetime

from django.test import TestCase
from django.utils import timezone

from.models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() renvoie False pour les questions dont le pub_date
        est dans l'avenir.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
```

Ici, nous avons créé une sous-classe de `django.test.TestCase` avec une méthode qui crée une instance de `Question` avec un `pub_date` dans l'avenir. Nous vérifions ensuite la sortie de `was_published_recently()` - qui _devrait_ être `False`.

## Exécuter les tests

Dans le terminal, nous pouvons exécuter notre test :

```bash
python manage.py test polls
```

Et vous verrez quelque chose comme :

```shell
[object Object]
```

> Erreur différente?

Si au lieu de cela vous obtenez une `NameError` ici, vous avez peut-être omis une étape dans la partie 2 <tutorial02-import-timezone> où nous avons ajouté les importations de `datetime` et `timezone` à `polls/models.py`. Copiez les importations de cette section et essayez de lancer à nouveau vos tests.

Voici ce qui s'est passé :

- `manage.py test polls` a cherché des tests dans l'application `polls`
- il a trouvé une sous-classe de la classe `django.test.TestCase`
- il a créé une base de données spéciale à des fins de test
- il a cherché des méthodes de test - celles dont les noms commencent par `test`
- dans `test_was_published_recently_with_future_question` il a créé une instance de `Question` dont le champ `pub_date` est dans 30 jours
  -... et en utilisant la méthode `assertIs()`, il a découvert que sa `was_published_recently()` renvoie `True`, alors que nous souhaitions qu'elle renvoie `False`

Le test nous informe de quel test a échoué et même de la ligne sur laquelle l'échec s'est produit.

## Corriger le bogue

Nous savons déjà quel est le problème : `Question.was_published_recently()` devrait renvoyer `False` si son `pub_date` est dans l'avenir. Modifiez la méthode dans `models.py` de sorte qu'elle ne renvoie `True` que si la date est également dans le passé :

```python
def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now
```

Et exécutez le test à nouveau :

```bash
Création de la base de données de test pour l'alias 'default'...
La vérification systématique n'a identifié aucun problème (0 silencés).
.
----------------------------------------------------------------------
1 test exécuté en 0,001s

OK
Destruction de la base de données de test pour l'alias 'default'...
```

Après avoir identifié un bogue, nous avons écrit un test qui le démasque et corrigé le bogue dans le code de sorte que notre test passe.

De nombreuses autres choses pourraient se produire dans notre application à l'avenir, mais nous pouvons être sûrs que nous ne réintroduirons pas accidentellement ce bogue, car exécuter le test nous avertira immédiatement. Nous pouvons considérer cette petite partie de l'application comme étant solidement fixée pour toujours.

## Tests plus complets

Pendant que nous sommes là, nous pouvons préciser davantage la méthode `was_published_recently()` ; en fait, il serait plutôt gênant si en corrigant un bogue nous avions introduit un autre.

Ajoutez deux autres méthodes de test à la même classe pour tester le comportement de la méthode de manière plus complète :

```python
def test_was_published_recently_with_old_question(self):
    """
    was_published_recently() renvoie False pour les questions dont le pub_date
    est antérieur à 1 jour.
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_question = Question(pub_date=time)
    self.assertIs(old_question.was_published_recently(), False)


def test_was_published_recently_with_recent_question(self):
    """
    was_published_recently() renvoie True pour les questions dont le pub_date
    est dans le dernier jour.
    """
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_question = Question(pub_date=time)
    self.assertIs(recent_question.was_published_recently(), True)
```

Et maintenant, nous avons trois tests qui confirment que `Question.was_published_recently()` renvoie des valeurs sensées pour les questions passées, récentes et futures.

Encore une fois, `polls` est une application minimale, mais quelle que soit la complexité qu'elle atteint à l'avenir et quelle que soit l'autre code avec lequel elle interagit, nous avons maintenant une certaine garantie que la méthode pour laquelle nous avons écrit des tests se comportera comme prévu.
