# Création de modèles

Maintenant, nous allons définir vos modèles - essentiellement, la structure de votre base de données, avec des métadonnées supplémentaires.

Un modèle est la source unique et définitive d'informations sur vos données. Il contient les champs essentiels et les comportements des données que vous stockez. Django suit le `Principe DRY <dry>`. L'objectif est de définir votre modèle de données à un seul endroit et de dériver automatiquement les choses à partir de celui-ci.

Cela inclut les migrations - contrairement à Ruby On Rails, par exemple, les migrations sont entièrement dérivées de votre fichier de modèles et sont essentiellement une histoire que Django peut parcourir pour mettre à jour votre schéma de base de données pour qu'il corresponde à vos modèles actuels.

Dans notre application de sondage, nous allons créer deux modèles : `Question` et `Choice`. Une `Question` a une question et une date de publication. Un `Choice` a deux champs : le texte du choix et un compteur de votes. Chaque `Choice` est associé à une `Question`.

Ces concepts sont représentés par des classes Python. Éditez le fichier `polls/models.py` pour qu'il ressemble à ceci :

```python
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

Ici, chaque modèle est représenté par une classe qui hérite de `django.db.models.Model`. Chaque modèle a un certain nombre de variables de classe, chacune représentant un champ de base de données dans le modèle.

Chaque champ est représenté par une instance d'une classe `~django.db.models.Field` - par exemple, `~django.db.models.CharField` pour les champs de caractères et `~django.db.models.DateTimeField` pour les dates et heures. Cela indique à Django quel type de données chaque champ contient.

Le nom de chaque instance de `~django.db.models.Field` (par exemple `question_text` ou `pub_date`) est le nom du champ, au format convivial pour les machines. Vous utiliserez cette valeur dans votre code Python, et votre base de données l'utilisera comme nom de colonne.

Vous pouvez utiliser un premier argument positionnel optionnel d'un `~django.db.models.Field` pour désigner un nom lisible par l'homme. Cela est utilisé dans plusieurs parties introspectives de Django et sert également de documentation. Si ce champ n'est pas fourni, Django utilisera le nom lisible par les machines. Dans cet exemple, nous avons seulement défini un nom lisible par l'homme pour `Question.pub_date`. Pour tous les autres champs de ce modèle, le nom lisible par les machines du champ suffira comme nom lisible par l'homme.

Certaines classes `~django.db.models.Field` ont des arguments requis. `~django.db.models.CharField`, par exemple, nécessite que vous lui donniez un `~django.db.models.CharField.max_length`. Cela est utilisé non seulement dans le schéma de base de données, mais également dans la validation, comme nous le verrons bientôt.

Un `~django.db.models.Field` peut également avoir divers arguments optionnels ; dans ce cas, nous avons défini la valeur `~django.db.models.Field.default` de `votes` sur 0.

Enfin, notez qu'une relation est définie, en utilisant `~django.db.models.ForeignKey`. Cela indique à Django que chaque `Choice` est lié à une seule `Question`. Django prend en charge toutes les relations de base de données courantes : plusieurs-vers-un, plusieurs-vers-plusieurs et un-vers-un.
