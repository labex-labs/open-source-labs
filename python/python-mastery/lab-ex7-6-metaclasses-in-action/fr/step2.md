# Collecter les types de validateurs

En Python, les validateurs sont des classes qui nous aident à nous assurer que les données répondent à certains critères. Notre première tâche dans cette expérience est de modifier la classe de base `Validator` afin qu'elle puisse collecter toutes ses sous - classes. Pourquoi devons - nous faire cela ? Eh bien, en collectant toutes les sous - classes de validateurs, nous pouvons créer un espace de noms qui contient tous les types de validateurs. Plus tard, nous injecterons cet espace de noms dans la classe `Structure`, ce qui nous facilitera la gestion et l'utilisation de différents validateurs.

Maintenant, commençons à travailler sur le code. Ouvrez le fichier `validate.py`. Vous pouvez utiliser la commande suivante dans le terminal pour l'ouvrir :

```bash
code validate.py
```

Une fois le fichier ouvert, nous devons ajouter un dictionnaire au niveau de la classe et une méthode `__init_subclass__()` à la classe `Validator`. Le dictionnaire au niveau de la classe sera utilisé pour stocker toutes les sous - classes de validateurs, et la méthode `__init_subclass__()` est une méthode spéciale en Python qui est appelée chaque fois qu'une sous - classe de la classe actuelle est définie.

Ajoutez le code suivant à la classe `Validator`, juste après la définition de la classe :

```python
# Add this to the Validator class in validate.py
validators = {}  # Dictionary to collect all validator subclasses

@classmethod
def __init_subclass__(cls):
    """Register each validator subclass in the validators dictionary"""
    Validator.validators[cls.__name__] = cls
```

Après avoir ajouté le code, votre classe `Validator` modifiée devrait maintenant ressembler à ceci :

```python
class Validator:
    validators = {}  # Dictionary to collect all validator subclasses

    @classmethod
    def __init_subclass__(cls):
        """Register each validator subclass in the validators dictionary"""
        Validator.validators[cls.__name__] = cls

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.name] = value

    def validate(self, value):
        pass
```

Maintenant, chaque fois qu'un nouveau type de validateur est défini, comme `String` ou `PositiveInteger`, Python appellera automatiquement la méthode `__init_subclass__()`. Cette méthode ajoutera ensuite la nouvelle sous - classe de validateur au dictionnaire `validators`, en utilisant le nom de la classe comme clé.

Vérifions si notre code fonctionne. Nous allons créer un simple script Python pour vérifier le contenu du dictionnaire `validators`. Vous pouvez exécuter la commande suivante dans le terminal :

```bash
python3 -c "from validate import Validator; print(Validator.validators)"
```

Si tout fonctionne correctement, vous devriez voir une sortie similaire à celle - ci, montrant tous les types de validateurs et les classes correspondantes :

```
{'Typed': <class 'validate.Typed'>, 'Positive': <class 'validate.Positive'>, 'NonEmpty': <class 'validate.NonEmpty'>, 'String': <class 'validate.String'>, 'Integer': <class 'validate.Integer'>, 'Float': <class 'validate.Float'>, 'PositiveInteger': <class 'validate.PositiveInteger'>, 'PositiveFloat': <class 'validate.PositiveFloat'>, 'NonEmptyString': <class 'validate.NonEmptyString'>}
```

Maintenant que nous avons un dictionnaire contenant tous nos types de validateurs, nous pouvons l'utiliser à l'étape suivante pour créer notre métaclasse.
