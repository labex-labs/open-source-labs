# Application de décorateurs via l'héritage

Dans l'Étape 2, nous avons créé un décorateur de classe qui simplifie notre code. Un décorateur de classe est un type spécial de fonction qui prend une classe en argument et retourne une classe modifiée. C'est un outil utile en Python pour ajouter des fonctionnalités aux classes sans modifier leur code d'origine. Cependant, nous devons toujours appliquer explicitement le décorateur `@validate_attributes` à chaque classe. Cela signifie que chaque fois que nous créons une nouvelle classe qui nécessite une validation, nous devons nous souvenir d'ajouter ce décorateur, ce qui peut être un peu fastidieux.

Nous pouvons améliorer cela en appliquant le décorateur automatiquement par héritage. L'héritage est un concept fondamental en programmation orientée objet où une sous - classe peut hériter d'attributs et de méthodes d'une classe mère. La méthode `__init_subclass__` de Python a été introduite en Python 3.6 pour permettre aux classes mères de personnaliser l'initialisation des sous - classes. Cela signifie que lorsqu'une sous - classe est créée, la classe mère peut effectuer certaines actions sur elle. Nous pouvons utiliser cette fonctionnalité pour appliquer automatiquement notre décorateur à toute classe qui hérite de `Structure`.

Implémentons cela :

1. Ouvrez le fichier `structure.py` :

```bash
code ~/project/structure.py
```

Ici, nous utilisons la commande `code` pour ouvrir le fichier `structure.py` dans un éditeur de code. Ce fichier contient la définition de la classe `Structure`, et nous allons la modifier pour utiliser la méthode `__init_subclass__`.

2. Ajoutez la méthode `__init_subclass__` à la classe `Structure` :

```python
class Structure:
    _fields = ()
    _types = ()

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, name, val)

    def __repr__(self):
        values = ', '.join(repr(getattr(self, name)) for name in self._fields)
        return f'{type(self).__name__}({values})'

    @classmethod
    def create_init(cls):
        '''
        Create an __init__ method from _fields
        '''
        body = 'def __init__(self, %s):\n' % ', '.join(cls._fields)
        for name in cls._fields:
            body += f'    self.{name} = {name}\n'

        # Execute the function creation code
        namespace = {}
        exec(body, namespace)
        setattr(cls, '__init__', namespace['__init__'])

    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)
```

La méthode `__init_subclass__` est une méthode de classe, ce qui signifie qu'elle peut être appelée sur la classe elle - même plutôt que sur une instance de la classe. Lorsqu'une sous - classe de `Structure` est créée, cette méthode sera automatiquement appelée. À l'intérieur de cette méthode, nous appelons le décorateur `validate_attributes` sur la sous - classe `cls`. De cette façon, chaque sous - classe de `Structure` aura automatiquement le comportement de validation.

3. Enregistrez le fichier.

Après avoir apporté des modifications au fichier `structure.py`, nous devons l'enregistrer pour que les modifications soient appliquées.

4. Maintenant, mettons à jour notre fichier `stock.py` pour tirer parti de cette nouvelle fonctionnalité :

```bash
code ~/project/stock.py
```

Nous ouvrons le fichier `stock.py` pour le modifier. Ce fichier contient la définition de la classe `Stock`, et nous allons la faire hériter de la classe `Structure` pour utiliser l'application automatique du décorateur.

5. Modifiez le fichier `stock.py` pour supprimer le décorateur explicite :

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

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

Notez que nous :

- Avons supprimé l'import de `validate_attributes` car nous n'avons plus besoin de l'importer explicitement puisque le décorateur est appliqué automatiquement par héritage.
- Avons supprimé le décorateur `@validate_attributes` car la méthode `__init_subclass__` de la classe `Structure` s'en occupera.
- Le code dépend maintenant uniquement de l'héritage de `Structure` pour obtenir le comportement de validation.

6. Exécutez les tests à nouveau pour vérifier que tout fonctionne toujours :

```bash
cd ~/project
python3 teststock.py
```

Exécuter les tests est important pour nous assurer que nos modifications n'ont rien cassé. Si tous les tests passent, cela signifie que l'application automatique du décorateur par héritage fonctionne correctement.

Vous devriez voir tous les tests passer :

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

Testons à nouveau notre classe `Stock` pour nous assurer qu'elle fonctionne comme prévu :

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

Cette commande crée une instance de la classe `Stock` et affiche sa représentation et le coût. Si la sortie est conforme aux attentes, cela signifie que la classe `Stock` fonctionne correctement avec l'application automatique du décorateur.

Sortie :

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

Cette implémentation est encore plus propre ! En utilisant `__init_subclass__`, nous avons éliminé le besoin d'appliquer explicitement des décorateurs. Toute classe qui hérite de `Structure` obtient automatiquement le comportement de validation.
