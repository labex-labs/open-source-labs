# Tests unitaires avec des erreurs attendues

Supposons que vous vouliez écrire un test unitaire qui vérifie une exception. Voici comment vous pouvez le faire :

```python
class TestStock(unittest.TestCase):
  ...
    def test_bad_shares(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
             s.shares = '50'
  ...
```

En utilisant ce test comme guide, écrivez des tests unitaires pour les modes de défaillance suivants :

- Testez que définir `shares` sur une chaîne de caractères lève une `TypeError`.
- Testez que définir `shares` sur un nombre négatif lève une `ValueError`.
- Testez que définir `price` sur une chaîne de caractères lève une `TypeError`.
- Testez que définir `price` sur un nombre négatif lève une `ValueError`.
- Testez que définir un attribut inexistant `share` lève une `AttributeError`.

En tout, vous devriez avoir environ une douzaine de tests unitaires lorsque vous aurez terminé.

**Note importante**

Pour une utilisation ultérieure dans le cours, vous voudrez avoir un fichier `stock.py` et `teststock.py` entièrement fonctionnels. Enregistrez votre travail en cours si nécessaire, mais vous êtes fortement encouragé à copier le code de `Solutions/5_6` si les choses ne fonctionnent toujours pas à ce stade.

Nous allons utiliser le fichier `teststock.py` comme outil pour améliorer le code `Stock` plus tard. Vous voudrez l'avoir à portée de main pour vous assurer que le nouveau code se comporte de la même manière que l'ancien.
