# Création de votre premier test unitaire

Le module `unittest` de Python est un outil puissant qui propose une manière structurée d'organiser et d'exécuter des tests. Avant de plonger dans l'écriture de notre premier test unitaire, comprenons quelques concepts clés. Les fixtures de test (test fixtures) sont des méthodes telles que `setUp` et `tearDown` qui aident à préparer l'environnement avant un test et à le nettoyer ensuite. Les cas de test (test cases) sont des unités individuelles de test, les suites de test (test suites) sont des collections de cas de test, et les exécuteurs de test (test runners) sont chargés d'exécuter ces tests et de présenter les résultats.

Dans cette première étape, nous allons créer un fichier de test de base pour la classe `Stock`, qui est déjà définie dans le fichier `stock.py`.

1. Tout d'abord, ouvrons le fichier `stock.py`. Cela nous aidera à comprendre la classe `Stock` que nous allons tester. En regardant le code dans `stock.py`, nous pouvons voir comment la classe est structurée, quelles sont ses attributs et quelles méthodes elle propose. Pour afficher le contenu du fichier `stock.py`, exécutez la commande suivante dans votre terminal :

```bash
cat stock.py
```

2. Maintenant, il est temps de créer un nouveau fichier nommé `teststock.py` en utilisant votre éditeur de texte préféré. Ce fichier contiendra nos cas de test pour la classe `Stock`. Voici le code que vous devez écrire dans le fichier `teststock.py` :

```python
# teststock.py

import unittest
import stock

class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

if __name__ == '__main__':
    unittest.main()
```

Décortiquons les éléments clés de ce code :

- `import unittest` : Cette ligne importe le module `unittest`, qui fournit les outils et les classes nécessaires pour écrire et exécuter des tests en Python.
- `import stock` : Cela importe le module qui contient notre classe `Stock`. Sans cette importation, nous ne pourrions pas accéder à la classe `Stock` dans notre code de test.
- `class TestStock(unittest.TestCase)` : Nous créons une nouvelle classe nommée `TestStock` qui hérite de `unittest.TestCase`. Cela fait de notre classe `TestStock` une classe de cas de test, qui peut contenir plusieurs méthodes de test.
- `def test_create(self)` : Il s'agit d'une méthode de test. Dans le cadre (framework) `unittest`, toutes les méthodes de test doivent commencer par le préfixe `test_`. Cette méthode crée une instance de la classe `Stock`, puis utilise la méthode `assertEqual` pour vérifier si les attributs de l'instance `Stock` correspondent aux valeurs attendues.
- `assertEqual` : C'est une méthode fournie par la classe `TestCase`. Elle vérifie si deux valeurs sont égales. Si elles ne sont pas égales, le test échouera.
- `unittest.main()` : Lorsque ce script est exécuté directement, `unittest.main()` exécutera toutes les méthodes de test de la classe `TestStock` et affichera les résultats.

3. Après avoir écrit le code dans le fichier `teststock.py`, enregistrez - le. Ensuite, exécutez la commande suivante dans votre terminal pour exécuter le test :

```bash
python3 teststock.py
```

Vous devriez voir une sortie similaire à ceci :

```
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```

Le point unique (`.`) dans la sortie indique qu'un test a réussi avec succès. Si un test échoue, vous verrez un `F` à la place du point, ainsi que des informations détaillées sur ce qui a mal fonctionné dans le test. Cette sortie vous aide à identifier rapidement si votre code fonctionne comme prévu ou s'il y a des problèmes à corriger.
