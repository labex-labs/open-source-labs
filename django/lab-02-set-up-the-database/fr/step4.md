# Expérimentons l'API

Maintenant, allons dans l'interpréteur de commandes Python interactif et testons l'API gratuite que Django vous offre. Pour invoquer l'interpréteur de commandes Python, utilisez cette commande :

```bash
python manage.py shell
```

Nous utilisons cela plutôt que de simplement taper "python" car `manage.py` définit la variable d'environnement `DJANGO_SETTINGS_MODULE`, qui fournit à Django le chemin d'importation Python vers votre fichier `mysite/settings.py`.

Une fois que vous êtes dans l'interpréteur de commandes, explorez l'`API de base de données </topics/db/queries>` :

```python
>>> from polls.models import Choice, Question  # Importez les classes de modèles que nous venons d'écrire.

# Il n'y a pas de questions dans le système pour le moment.
>>> Question.objects.all()
<QuerySet []>

# Créez une nouvelle Question.
# La prise en charge des fuseaux horaires est activée dans le fichier de paramètres par défaut, donc
# Django attend une date et heure avec une information de fuseau horaire pour pub_date. Utilisez timezone.now()
# au lieu de datetime.datetime.now() et cela fonctionnera correctement.
>>> from django.utils import timezone
>>> q = Question(question_text="Quoi de neuf?", pub_date=timezone.now())

# Enregistrez l'objet dans la base de données. Vous devez appeler save() explicitement.
>>> q.save()

# Maintenant, il a un ID.
>>> q.id
1

# Accédez aux valeurs des champs du modèle via des attributs Python.
>>> q.question_text
"Quoi de neuf?"
>>> q.pub_date
datetime.datetime(2023, 9, 7, 1, 18, 48, 335644, tzinfo=datetime.timezone.utc)

# Changez les valeurs en modifiant les attributs, puis appelez save().
>>> q.question_text = "Quoi de neuf?"
>>> q.save()

# objects.all() affiche toutes les questions dans la base de données.
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>
```

Attendez une minute. `<Question: Question object (1)>` n'est pas une représentation utile de cet objet. Corrigeons cela en modifiant le modèle `Question` (dans le fichier `polls/models.py`) et en ajoutant une méthode `~django.db.models.Model.__str__` à `Question` et `Choice` :

```python
from django.db import models


class Question(models.Model):
    #...
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    #...
    def __str__(self):
        return self.choice_text
```

Il est important d'ajouter des méthodes `~django.db.models.Model.__str__` à vos modèles, non seulement pour votre propre commodité lors de l'utilisation de l'interpréteur interactif, mais également parce que les représentations des objets sont utilisées dans tout l'administrateur automatiquement généré par Django.

Ajoutons également une méthode personnalisée à ce modèle :

```python
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    #...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
```

Notez l'ajout de `import datetime` et `from django.utils import timezone`, pour référencer respectivement le module `datetime` standard de Python et les utilitaires liés aux fuseaux horaires de Django dans `django.utils.timezone`. Si vous n'êtes pas familier avec la gestion des fuseaux horaires en Python, vous pouvez en apprendre plus dans la `documentation sur la prise en charge des fuseaux horaires </topics/i18n/timezones>`.

Enregistrez ces modifications et lancez un nouvel interpréteur interactif Python en **exécutant `python manage.py shell` à nouveau** :

```python
>>> from polls.models import Choice, Question

# Assurez-vous que notre ajout de __str__() a fonctionné.
>>> Question.objects.all()
<QuerySet [<Question: Quoi de neuf?>]>

# Django fournit une riche API de recherche de base de données entièrement basée sur
# des arguments clés.
>>> Question.objects.filter(id=1)
<QuerySet [<Question: Quoi de neuf?>]>
>>> Question.objects.filter(question_text__startswith="Quoi")
<QuerySet [<Question: Quoi de neuf?>]>

# Obtenez la question publiée cette année.
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: Quoi de neuf?>

# Demandez un ID qui n'existe pas, cela entraînera une exception.
>>> Question.objects.get(id=2)
Traceback (most recent call last):
 ...
DoesNotExist: Question matching query does not exist.

# La recherche par clé primaire est le cas le plus courant, donc Django fournit un
# raccourci pour les recherches exactes par clé primaire.
# Ce qui suit est identique à Question.objects.get(id=1).
>>> Question.objects.get(pk=1)
<Question: Quoi de neuf?>

# Assurez-vous que notre méthode personnalisée a fonctionné.
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# Donnez à la Question quelques Choix. L'appel create construit un nouveau
# objet Choice, exécute l'instruction INSERT, ajoute le choix à l'ensemble
# des choix disponibles et renvoie le nouveau objet Choice. Django crée
# un ensemble pour stocker l'autre côté d'une relation de clé étrangère
# (par exemple, les choix d'une question) qui peut être consulté via l'API.
>>> q = Question.objects.get(pk=1)

# Affichez tous les choix de l'ensemble d'objets liés - aucun pour le moment.
>>> q.choice_set.all()
<QuerySet []>

# Créez trois choix.
>>> q.choice_set.create(choice_text="Pas grand-chose", votes=0)
<Choice: Pas grand-chose>
>>> q.choice_set.create(choice_text="Le ciel", votes=0)
<Choice: Le ciel>
>>> c = q.choice_set.create(choice_text="En train de hacker encore", votes=0)

# Les objets Choice ont accès via l'API à leurs objets Question liés.
>>> c.question
<Question: Quoi de neuf?>

# Et vice versa : les objets Question ont accès aux objets Choice.
>>> q.choice_set.all()
<QuerySet [<Choice: Pas grand-chose>, <Choice: Le ciel>, <Choice: En train de hacker encore>]>
>>> q.choice_set.count()
3

# L'API suit automatiquement les relations aussi loin que nécessaire.
# Utilisez des doubles tirets pour séparer les relations.
# Cela fonctionne à plusieurs niveaux de profondeur que vous voulez ; il n'y a pas de limite.
# Trouvez tous les Choix pour toute question dont la pub_date est cette année
# (en réutilisant la variable 'current_year' que nous avons créée ci-dessus).
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Pas grand-chose>, <Choice: Le ciel>, <Choice: En train de hacker encore>]>

# Supprimons l'un des choix. Utilisez delete() pour cela.
>>> c = q.choice_set.filter(choice_text__startswith="En train de hacker")
>>> c.delete()
```

Pour plus d'informations sur les relations de modèles, consultez `Accès aux objets liés
</ref/models/relations>`. Pour en savoir plus sur la manière d'utiliser les doubles tirets pour effectuer des recherches de champs via l'API, consultez `Recherches de champs <field-lookups-intro>`. Pour plus de détails sur l'API de base de données, consultez notre `Référence de l'API de base de données
</topics/db/queries>`.
