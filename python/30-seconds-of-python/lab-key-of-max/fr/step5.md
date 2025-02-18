# Test avec des valeurs toutes négatives

En tant que dernier test, gérons un cas où toutes les valeurs du dictionnaire sont négatives. Ajoutez cette méthode à `TestKeyOfMax` :

```python
    def test_all_negative_values(self):
        self.assertEqual(key_of_max({'x': -5, 'y': -2, 'z': -10}), 'y')
```

Ce test garantit que notre fonction identifie correctement la valeur _la moins négative_ (qui est la valeur maximale dans ce cas) et renvoie la clé associée.

Exécutez vos tests une dernière fois (`python3 test_key_of_max.py`). Les quatre tests devraient réussir. Cela nous donne une forte confiance que notre fonction fonctionne correctement.

Votre fichier `test_key_of_max.py` complet devrait maintenant ressembler à ceci :

```python
import unittest
from key_of_max import key_of_max

class TestKeyOfMax(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(key_of_max({'a': 4, 'b': 0, 'c': 13}), 'c')

    def test_another_case(self):
        self.assertEqual(key_of_max({'apple': 10, 'banana': 5, 'orange': 10}), 'apple')

    def test_empty_dictionary(self):
        self.assertIsNone(key_of_max({}))

    def test_all_negative_values(self):
        self.assertEqual(key_of_max({'x': -5, 'y': -2, 'z': -10}), 'y')

if __name__ == '__main__':
    unittest.main()
```

Exécutez les tests à nouveau (`python3 test_key_of_max.py`). Les quatre tests devraient réussir. Cela nous donne une forte confiance que notre fonction fonctionne correctement.

```python
python3 test_key_of_max.py
```

```plaintext
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```
