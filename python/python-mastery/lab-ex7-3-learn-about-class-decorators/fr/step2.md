# Création d'un décorateur de classe pour la validation

Dans l'étape précédente, notre implémentation fonctionnait, mais il y avait une redondance. Nous devions spécifier à la fois le tuple `_fields` et les attributs descripteurs. Ce n'est pas très efficace, et nous pouvons l'améliorer. En Python, les décorateurs de classe sont un outil puissant qui peut nous aider à simplifier ce processus. Un décorateur de classe est une fonction qui prend une classe en argument, la modifie d'une certaine manière, puis retourne la classe modifiée. En utilisant un décorateur de classe, nous pouvons extraire automatiquement les informations de champ à partir des descripteurs, ce qui rendra notre code plus propre et plus facilement maintenable.

Créons un décorateur de classe pour simplifier notre code. Voici les étapes à suivre :

1. Tout d'abord, ouvrez le fichier `structure.py`. Vous pouvez utiliser la commande suivante dans le terminal :

```bash
code ~/project/structure.py
```

Cette commande ouvrira le fichier `structure.py` dans votre éditeur de code.

2. Ensuite, ajoutez le code suivant en haut du fichier `structure.py`, juste après les instructions d'importation. Ce code définit notre décorateur de classe :

```python
from validate import Validator

def validate_attributes(cls):
    """
    Class decorator that extracts Validator instances
    and builds the _fields list automatically
    """
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # Set _fields based on validator names
    cls._fields = [val.name for val in validators]

    # Create initialization method
    cls.create_init()

    return cls
```

Analysons ce que fait ce décorateur :

- Il crée d'abord une liste vide appelée `validators`. Ensuite, il itère sur tous les attributs de la classe en utilisant `vars(cls).items()`. Si un attribut est une instance de la classe `Validator`, il ajoute cet attribut à la liste `validators`.
- Après cela, il définit l'attribut `_fields` de la classe. Il crée une liste de noms à partir des validateurs de la liste `validators` et l'assigne à `cls._fields`.
- Enfin, il appelle la méthode `create_init()` de la classe pour générer la méthode `__init__`, puis retourne la classe modifiée.

3. Une fois que vous avez ajouté le code, enregistrez le fichier `structure.py`. Enregistrer le fichier garantit que vos modifications sont conservées.

4. Maintenant, nous devons modifier notre fichier `stock.py` pour utiliser ce nouveau décorateur. Ouvrez le fichier `stock.py` en utilisant la commande suivante :

```bash
code ~/project/stock.py
```

5. Mettez à jour le fichier `stock.py` pour utiliser le décorateur `validate_attributes`. Remplacez le code existant par le suivant :

```python
# stock.py

from structure import Structure, validate_attributes
from validate import String, PositiveInteger, PositiveFloat

@validate_attributes
class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

Remarquez les modifications que nous avons apportées :

- Nous avons ajouté le décorateur `@validate_attributes` juste au-dessus de la définition de la classe `Stock`. Cela indique à Python d'appliquer le décorateur `validate_attributes` à la classe `Stock`.
- Nous avons supprimé la déclaration explicite de `_fields` car le décorateur s'en occupera automatiquement.
- Nous avons également supprimé l'appel à `Stock.create_init()` car le décorateur s'occupe de créer la méthode `__init__`.

En conséquence, la classe est maintenant plus simple et plus propre. Le décorateur s'occupe de tous les détails que nous devions gérer manuellement.

6. Après avoir apporté ces modifications, nous devons vérifier que tout fonctionne toujours comme prévu. Exécutez les tests à nouveau en utilisant les commandes suivantes :

```bash
cd ~/project
python3 teststock.py
```

Si tout fonctionne correctement, vous devriez voir la sortie suivante :

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

Cette sortie indique que tous les tests ont réussi.

Testons également notre classe `Stock` de manière interactive. Exécutez la commande suivante dans le terminal :

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

Vous devriez voir la sortie suivante :

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

Super ! Vous avez réussi à implémenter un décorateur de classe qui simplifie notre code en gérant automatiquement les déclarations de champ et l'initialisation. Cela rend notre code plus efficace et plus facile à maintenir.
