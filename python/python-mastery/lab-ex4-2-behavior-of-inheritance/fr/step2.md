# Construction d'un système de validation avec l'héritage

Dans cette étape, nous allons construire un système de validation pratique en utilisant l'héritage. L'héritage est un concept puissant en programmation qui vous permet de créer de nouvelles classes basées sur des classes existantes. De cette manière, vous pouvez réutiliser le code et créer des programmes plus organisés et modulaires. En construisant ce système de validation, vous verrez comment l'héritage peut être utilisé pour créer des composants de code réutilisables qui peuvent être combinés de différentes manières.

## Création de la classe de base des validateurs

Tout d'abord, nous devons créer une classe de base pour nos validateurs. Pour ce faire, nous allons créer un nouveau fichier dans le WebIDE. Voici comment vous pouvez le faire : cliquez sur "File" > "New File", ou vous pouvez utiliser le raccourci clavier. Une fois le nouveau fichier ouvert, nommez - le `validate.py`.

Maintenant, ajoutons du code à ce fichier pour créer une classe de base `Validator`. Cette classe servira de fondation pour tous nos autres validateurs.

```python
# validate.py
class Validator:
    @classmethod
    def check(cls, value):
        return value
```

Dans ce code, nous avons défini une classe `Validator` avec une méthode `check`. La méthode `check` prend une valeur en argument et la renvoie simplement inchangée. Le décorateur `@classmethod` est utilisé pour transformer cette méthode en une méthode de classe. Cela signifie que nous pouvons appeler cette méthode sur la classe elle - même, sans avoir à créer une instance de la classe.

## Ajout de validateurs de type

Ensuite, nous allons ajouter des validateurs qui vérifient le type d'une valeur. Ces validateurs hériteront de la classe `Validator` que nous venons de créer. Revenez au fichier `validate.py` et ajoutez le code suivant :

```python
class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return super().check(value)

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str
```

La classe `Typed` est une sous - classe de `Validator`. Elle a un attribut `expected_type`, qui est initialement défini sur `object`. La méthode `check` dans la classe `Typed` vérifie si la valeur donnée est du type attendu. Si ce n'est pas le cas, elle lève une `TypeError`. Si le type est correct, elle appelle la méthode `check` de la classe parente en utilisant `super().check(value)`.

Les classes `Integer`, `Float` et `String` héritent de `Typed` et spécifient le type exact qu'elles sont censées vérifier. Par exemple, la classe `Integer` vérifie si une valeur est un entier.

## Test des validateurs de type

Maintenant que nous avons créé nos validateurs de type, testons - les. Ouvrez un nouveau terminal et lancez l'interpréteur Python en exécutant la commande suivante :

```bash
python3
```

Une fois que l'interpréteur Python est en cours d'exécution, nous pouvons importer et tester nos validateurs. Voici du code pour les tester :

```python
from validate import Integer, String

Integer.check(10)  # Should return 10

try:
    Integer.check('10')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")

String.check('10')  # Should return '10'
```

Lorsque vous exécutez ce code, vous devriez voir quelque chose comme ceci :

```
10
Error: Expected <class 'int'>
'10'
```

Nous pouvons également utiliser ces validateurs dans une fonction. Essayons cela :

```python
def add(x, y):
    Integer.check(x)
    Integer.check(y)
    return x + y

add(2, 2)  # Should return 4

try:
    add('2', '3')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")
```

Lorsque vous exécutez ce code, vous devriez voir :

```
4
Error: Expected <class 'int'>
```

## Ajout de validateurs de valeur

Jusqu'à présent, nous avons créé des validateurs qui vérifient le type d'une valeur. Maintenant, ajoutons des validateurs qui vérifient la valeur elle - même plutôt que le type. Revenez au fichier `validate.py` et ajoutez le code suivant :

```python
class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        return super().check(value)

class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('Must be non-empty')
        return super().check(value)
```

Le validateur `Positive` vérifie si une valeur est non négative. Si la valeur est inférieure à 0, il lève une `ValueError`. Le validateur `NonEmpty` vérifie si une valeur a une longueur non nulle. Si la longueur est 0, il lève une `ValueError`.

## Composition de validateurs avec l'héritage multiple

Maintenant, nous allons combiner nos validateurs en utilisant l'héritage multiple. L'héritage multiple permet à une classe d'hériter de plusieurs classes parentes. Revenez au fichier `validate.py` et ajoutez le code suivant :

```python
class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass
```

Ces nouvelles classes combinent la vérification de type et la vérification de valeur. Par exemple, la classe `PositiveInteger` vérifie qu'une valeur est à la fois un entier et non négative. L'ordre d'héritage est important ici. Les validateurs sont vérifiés dans l'ordre spécifié dans la définition de la classe.

## Test des validateurs composés

Testons nos validateurs composés. Dans l'interpréteur Python, exécutez le code suivant :

```python
from validate import PositiveInteger, PositiveFloat, NonEmptyString

PositiveInteger.check(10)  # Should return 10

try:
    PositiveInteger.check('10')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")

try:
    PositiveInteger.check(-10)  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")

NonEmptyString.check('hello')  # Should return 'hello'

try:
    NonEmptyString.check('')  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")
```

Lorsque vous exécutez ce code, vous devriez voir :

```
10
Error: Expected <class 'int'>
Error: Expected >= 0
'hello'
Error: Must be non-empty
```

Cela montre comment nous pouvons combiner des validateurs pour créer des règles de validation plus complexes.

Lorsque vous avez terminé de tester, vous pouvez quitter l'interpréteur Python en exécutant la commande suivante :

```python
exit()
```
