# Implémentation d'une classe de base abstraite

Dans cette étape, nous allons convertir la classe `TableFormatter` en une véritable classe de base abstraite (ABC - Abstract Base Class) en utilisant le module `abc` de Python. Mais d'abord, comprenons ce qu'est une classe de base abstraite et pourquoi nous en avons besoin.

## Comprendre les classes de base abstraites

Une classe de base abstraite est un type spécial de classe en Python. C'est une classe à partir de laquelle vous ne pouvez pas créer directement un objet, ce qui signifie que vous ne pouvez pas l'instancier. Le but principal d'une classe de base abstraite est de définir une interface commune pour ses sous - classes. Elle établit un ensemble de règles que toutes les sous - classes doivent suivre. Plus précisément, elle exige que les sous - classes implémentent certaines méthodes.

Voici quelques concepts clés concernant les classes de base abstraites :

- Nous utilisons le module `abc` en Python pour créer des classes de base abstraites.
- Les méthodes marquées avec le décorateur `@abstractmethod` sont comme des règles. Toute sous - classe qui hérite d'une classe de base abstraite doit implémenter ces méthodes.
- Si vous essayez de créer un objet d'une classe qui hérite d'une classe de base abstraite mais n'a pas implémenté toutes les méthodes requises, Python lèvera une erreur.

Maintenant que vous comprenez les bases des classes de base abstraites, voyons comment nous pouvons modifier la classe `TableFormatter` pour en faire une.

## Modification de la classe TableFormatter

Ouvrez le fichier `tableformat.py`. Nous allons apporter quelques modifications à la classe `TableFormatter` afin qu'elle utilise le module `abc` et devienne une classe de base abstraite.

1. Tout d'abord, nous devons importer les éléments nécessaires du module `abc`. Ajoutez l'instruction d'importation suivante en haut du fichier :

```python
# tableformat.py
from abc import ABC, abstractmethod
```

Cette instruction d'importation importe deux éléments importants : `ABC`, qui est une classe de base pour toutes les classes de base abstraites en Python, et `abstractmethod`, qui est un décorateur que nous utiliserons pour marquer les méthodes comme abstraites.

2. Ensuite, nous allons modifier la classe `TableFormatter`. Elle doit hériter de `ABC` pour devenir une classe de base abstraite, et nous allons marquer ses méthodes comme abstraites en utilisant le décorateur `@abstractmethod`. Voici à quoi la classe modifiée devrait ressembler :

```python
class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        pass

    @abstractmethod
    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        pass
```

Remarquez quelques points concernant cette classe modifiée :

- La classe hérite maintenant de `ABC`, ce qui signifie qu'elle est officiellement une classe de base abstraite.
- Les méthodes `headings` et `row` sont toutes deux décorées avec `@abstractmethod`. Cela indique à Python que toute sous - classe de `TableFormatter` doit implémenter ces méthodes.
- Nous avons remplacé `NotImplementedError` par `pass`. Le décorateur `@abstractmethod` s'occupe de s'assurer que les sous - classes implémentent ces méthodes, nous n'avons donc plus besoin de `NotImplementedError`.

## Test de votre classe de base abstraite

Maintenant que nous avons transformé la classe `TableFormatter` en une classe de base abstraite, testons si elle fonctionne correctement. Nous allons créer un fichier appelé `test_abc.py` avec le code suivant :

```python
from tableformat import TableFormatter

# Test case 1: Define a class with a misspelled method
try:
    class NewFormatter(TableFormatter):
        def headers(self, headings):  # Misspelled 'headings'
            pass
        def row(self, rowdata):
            pass

    f = NewFormatter()
    print("Test 1 failed - abstract method enforcement not working")
except TypeError as e:
    print(f"Test 1 passed - caught error: {e}")

# Test case 2: Define a class that properly implements all methods
try:
    class ProperFormatter(TableFormatter):
        def headings(self, headers):
            pass
        def row(self, rowdata):
            pass

    f = ProperFormatter()
    print("Test 2 passed - proper implementation works")
except TypeError as e:
    print(f"Test 2 failed - error: {e}")
```

Dans ce code, nous avons deux cas de test. Le premier cas de test définit une classe `NewFormatter` qui tente d'hériter de `TableFormatter` mais a un nom de méthode mal orthographié. Le deuxième cas de test définit une classe `ProperFormatter` qui implémente correctement toutes les méthodes requises.

Pour exécuter le test, ouvrez votre terminal et exécutez la commande suivante :

```bash
python test_abc.py
```

Vous devriez voir une sortie similaire à celle - ci :

```
Test 1 passed - caught error: Can't instantiate abstract class NewFormatter with abstract methods headings
Test 2 passed - proper implementation works
```

Cette sortie confirme que notre classe de base abstraite fonctionne comme prévu. Le premier cas de test échoue car la classe `NewFormatter` n'a pas implémenté correctement la méthode `headings`. Le deuxième cas de test réussit car la classe `ProperFormatter` a implémenté toutes les méthodes requises.
