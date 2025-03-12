# Ajout de la validation des arguments de méthode

En Python, la validation des données est une partie importante de l'écriture de code robuste. Dans cette section, nous allons pousser notre validation plus loin en validant automatiquement les arguments des méthodes. Le fichier `validate.py` inclut déjà un décorateur `@validated`. Un décorateur en Python est une fonction spéciale qui peut modifier une autre fonction. Le décorateur `@validated` ici peut vérifier les arguments d'une fonction par rapport à leurs annotations. Les annotations en Python sont un moyen d'ajouter des métadonnées aux paramètres et aux valeurs de retour des fonctions.

Modifions notre code pour appliquer ce décorateur aux méthodes avec des annotations :

1. Tout d'abord, nous devons comprendre comment le décorateur `validated` fonctionne. Ouvrez le fichier `validate.py` pour le réviser :

```bash
code ~/project/validate.py
```

Le décorateur `validated` utilise les annotations de fonction pour valider les arguments. Avant de permettre à la fonction de s'exécuter, il vérifie chaque argument par rapport à son type d'annotation. Par exemple, si un argument est annoté comme un entier, le décorateur s'assurera que la valeur passée est bien un entier.

2. Maintenant, nous allons modifier la fonction `validate_attributes` dans `structure.py` pour envelopper les méthodes annotées avec le décorateur `validated`. Cela signifie que toute méthode avec des annotations dans la classe aura ses arguments automatiquement validés. Ouvrez le fichier `structure.py` :

```bash
code ~/project/structure.py
```

3. Mettez à jour la fonction `validate_attributes` :

```python
def validate_attributes(cls):
    """
    Class decorator that:
    1. Extracts Validator instances and builds _fields and _types lists
    2. Applies @validated decorator to methods with annotations
    """
    # Import the validated decorator
    from validate import validated

    # Process validator descriptors
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # Set _fields based on validator names
    cls._fields = [val.name for val in validators]

    # Set _types based on validator expected_types
    cls._types = [getattr(val, 'expected_type', lambda x: x) for val in validators]

    # Apply @validated decorator to methods with annotations
    for name, val in vars(cls).items():
        if callable(val) and hasattr(val, '__annotations__'):
            setattr(cls, name, validated(val))

    # Create initialization method
    cls.create_init()

    return cls
```

Cette fonction mise à jour fait maintenant les choses suivantes :

1. Elle traite les descripteurs de validateurs comme avant. Les descripteurs de validateurs sont utilisés pour définir les règles de validation des attributs de classe.
2. Elle trouve toutes les méthodes avec des annotations dans la classe. Les annotations sont ajoutées aux paramètres de méthode pour spécifier le type attendu de l'argument.
3. Elle applique le décorateur `@validated` à ces méthodes. Cela garantit que les arguments passés à ces méthodes sont validés selon leurs annotations.

4. Enregistrez le fichier après avoir apporté ces modifications. Enregistrer le fichier est important car cela assure que nos modifications sont stockées et peuvent être utilisées plus tard.

5. Maintenant, mettons à jour la méthode `sell` dans la classe `Stock` pour inclure une annotation. Les annotations aident à spécifier le type attendu de l'argument, qui sera utilisé par le décorateur `@validated` pour la validation. Ouvrez le fichier `stock.py` :

```bash
code ~/project/stock.py
```

6. Modifiez la méthode `sell` pour inclure une annotation de type :

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

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

Le changement important est l'ajout de `: PositiveInteger` au paramètre `nshares`. Cela indique à Python (et à notre décorateur `@validated`) de valider cet argument en utilisant le validateur `PositiveInteger`. Ainsi, lorsque nous appelons la méthode `sell`, l'argument `nshares` doit être un entier positif.

7. Exécutez les tests à nouveau pour vérifier que tout fonctionne toujours. Exécuter des tests est un bon moyen de nous assurer que nos modifications n'ont pas cassé une fonctionnalité existante.

```bash
cd ~/project
python3 teststock.py
```

Vous devriez voir tous les tests passer :

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

8. Testons notre nouvelle validation d'arguments. Nous allons essayer d'appeler la méthode `sell` avec des arguments valides et invalides pour voir si la validation fonctionne comme prévu.

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); s.sell(25); print(s); try: s.sell(-25); except Exception as e: print(f'Error: {e}')"
```

Vous devriez voir une sortie similaire à :

```
Stock('GOOG', 75, 490.1)
Error: Bad Arguments
  nshares: must be >= 0
```

Cela montre que notre validation d'arguments de méthode fonctionne ! Le premier appel à `sell(25)` réussit car `25` est un entier positif. Mais le deuxième appel à `sell(-25)` échoue car `-25` n'est pas un entier positif.

Vous avez maintenant implémenté un système complet pour :

1. Valider les attributs de classe en utilisant des descripteurs. Les descripteurs sont utilisés pour définir les règles de validation des attributs de classe.
2. Collecter automatiquement les informations de champ en utilisant des décorateurs de classe. Les décorateurs de classe peuvent modifier le comportement d'une classe, comme collecter les informations de champ.
3. Convertir les données de ligne en instances. Cela est utile lorsque vous travaillez avec des données provenant de sources externes.
4. Valider les arguments de méthode en utilisant des annotations. Les annotations aident à spécifier le type attendu de l'argument pour la validation.

Cela démontre la puissance de combiner les descripteurs et les décorateurs en Python pour créer des classes expressives et auto - validantes.
