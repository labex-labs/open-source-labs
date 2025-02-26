# Module `unittest`

Supposons que vous ayez du code dans `simple.py`.

```python
# simple.py

def add(x, y):
    return x + y
```

Maintenant, supposons que vous vouliez le tester. Créez un fichier de test séparé comme ceci dans `/home/labex/project/test_simple.py`.

```python
# test_simple.py

import simple
import unittest
```

Ensuite, définissez une classe de test.

```python
# test_simple.py

import simple
import unittest

# Remarquez qu'elle hérite de unittest.TestCase
class TestAdd(unittest.TestCase):
  ...
```

La classe de test doit hériter de `unittest.TestCase`.

Dans la classe de test, vous définissez les méthodes de test.

```python
# test_simple.py

import simple
import unittest

# Remarquez qu'elle hérite de unittest.TestCase
class TestAdd(unittest.TestCase):
    def test_simple(self):
        # Test avec des arguments entiers simples
        r = simple.add(2, 2)
        self.assertEqual(r, 5)
    def test_str(self):
        # Test avec des chaînes de caractères
        r = simple.add('hello', 'world')
        self.assertEqual(r, 'helloworld')
```

\*Important : Chaque méthode doit commencer par `test`.
