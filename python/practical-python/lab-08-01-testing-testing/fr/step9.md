# Exercice 8.1 : Écrire des tests unitaires

Dans un fichier séparé `test_stock.py`, écrivez un ensemble de tests unitaires pour la classe `Stock`. Pour vous aider à commencer, voici un petit fragment de code qui teste la création d'instances :

```python
# test_stock.py

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

Exécutez vos tests unitaires. Vous devriez obtenir une sortie qui ressemble à ceci :

## .

Ran 1 tests in 0.000s

    OK

Une fois que vous êtes satisfait que cela fonctionne, écrivez d'autres tests unitaires qui vérifient les points suivants :

- Vérifiez que la propriété `s.cost` renvoie la valeur correcte (49010.0)
- Vérifiez que la méthode `s.sell()` fonctionne correctement. Elle devrait décrémenter la valeur de `s.shares` en conséquence.
- Vérifiez que l'attribut `s.shares` ne peut pas être défini sur une valeur non entière.

Pour la dernière partie, vous devrez vérifier qu'une exception est levée. Un moyen simple de le faire est avec du code comme ceci :

```python
class TestStock(unittest.TestCase):
  ...
    def test_bad_shares(self):
         s = stock.Stock('GOOG', 100, 490.1)
         with self.assertRaises(TypeError):
             s.shares = '100'
```
