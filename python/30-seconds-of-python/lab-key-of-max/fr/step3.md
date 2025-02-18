# Création de tests unitaires : tests de base

Maintenant, écrivons quelques tests pour nous assurer que notre fonction fonctionne correctement. Nous allons utiliser le module `unittest` de Python. Créez un nouveau fichier nommé `test_key_of_max.py` et ajoutez le code suivant :

```python
import unittest
from key_of_max import key_of_max  # Import our function

class TestKeyOfMax(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(key_of_max({'a': 4, 'b': 0, 'c': 13}), 'c')

    def test_another_case(self):
        self.assertEqual(key_of_max({'apple': 10, 'banana': 5, 'orange': 10}), 'apple')

if __name__ == '__main__':
    unittest.main()
```

Explication :

1.  **`import unittest`** : Importe le framework de test.
2.  **`from key_of_max import key_of_max`** : Importe la fonction que nous voulons tester.
3.  **`class TestKeyOfMax(unittest.TestCase):`** : Définit une _classe de test_. Les classes de test regroupent des tests liés.
4.  **`def test_basic_case(self):`** : Définit une _méthode de test_. Chaque méthode de test vérifie un aspect spécifique de notre fonction. Les noms des méthodes de test _doivent_ commencer par `test_`.
5.  **`self.assertEqual(...)`** : C'est une _assertion_. Elle vérifie si deux valeurs sont égales. Si elles ne sont pas égales, le test échoue. Dans ce cas, nous vérifions si `key_of_max({'a': 4, 'b': 0, 'c': 13})` renvoie `'c'`, ce qu'il devrait faire.
6.  **`def test_another_case(self):`** : Ajout d'un autre cas de test pour vérifier la clé de la valeur maximale qui peut ne pas être unique.
7.  **`if __name__ == '__main__': unittest.main()`** : Ce code Python standard exécute les tests lorsque vous exécutez le script directement (par exemple, `python3 test_key_of_max.py`).

Exécutez les tests depuis votre terminal : `python3 test_key_of_max.py`. Vous devriez voir un résultat indiquant que les deux tests ont réussi.

```python
python3 test_key_of_max.py
```

```plaintext
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
