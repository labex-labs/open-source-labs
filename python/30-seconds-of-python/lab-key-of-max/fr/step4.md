# Test du dictionnaire vide (cas limite)

Ajoutons un test spécifiquement pour le cas du dictionnaire vide. Ajoutez cette méthode à votre classe `TestKeyOfMax` dans `test_key_of_max.py` :

```python
    def test_empty_dictionary(self):
        self.assertIsNone(key_of_max({}))
```

- **`self.assertIsNone(...)`** : Cette assertion vérifie si la valeur est spécifiquement `None`. Cela est important car `self.assertEqual(..., None)` pourrait réussir pour des éléments qui _s'évaluent_ à `None`, mais qui ne sont pas réellement `None`. `assertIsNone` est plus strict.

Exécutez les tests à nouveau (`python3 test_key_of_max.py`). Les trois tests (les deux tests de base et le test du dictionnaire vide) devraient maintenant réussir.

```python
python3 test_key_of_max.py
```

```plaintext
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```
