# Test des exceptions

Le test est une partie cruciale du développement logiciel, et un aspect important consiste à s'assurer que votre code peut gérer correctement les conditions d'erreur. En Python, le module `unittest` offre un moyen pratique de tester si des exceptions spécifiques sont levées comme prévu.

1. Ouvrez le fichier `teststock.py`. Nous allons ajouter quelques méthodes de test conçues pour vérifier les exceptions. Ces tests nous aideront à nous assurer que notre code se comporte correctement lorsqu'il rencontre des entrées invalides.

```python
def test_shares_type(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(TypeError):
        s.shares = '50'

def test_shares_value(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(ValueError):
        s.shares = -50

def test_price_type(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(TypeError):
        s.price = '490.1'

def test_price_value(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(ValueError):
        s.price = -490.1

def test_attribute_error(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(AttributeError):
        s.share = 100  # 'share' is incorrect, should be 'shares'
```

Comprenons maintenant comment fonctionnent ces tests d'exceptions.

- La déclaration `with self.assertRaises(ExceptionType):` crée un gestionnaire de contexte (context manager). Ce gestionnaire de contexte vérifie si le code à l'intérieur du bloc `with` lève l'exception spécifiée.
- Si l'exception attendue est levée à l'intérieur du bloc `with`, le test réussit. Cela signifie que notre code détecte correctement l'entrée invalide et lève l'erreur appropriée.
- Si aucune exception n'est levée ou si une autre exception est levée, le test échoue. Cela indique que notre code peut ne pas gérer l'entrée invalide comme prévu.

Ces tests sont conçus pour vérifier les scénarios suivants :

- Définir l'attribut `shares` sur une chaîne de caractères devrait lever une `TypeError` car `shares` devrait être un nombre.
- Définir l'attribut `shares` sur un nombre négatif devrait lever une `ValueError` car le nombre d'actions ne peut pas être négatif.
- Définir l'attribut `price` sur une chaîne de caractères devrait lever une `TypeError` car `price` devrait être un nombre.
- Définir l'attribut `price` sur un nombre négatif devrait lever une `ValueError` car le prix ne peut pas être négatif.
- Tenter de définir un attribut inexistant `share` (notez l'absence de 's') devrait lever une `AttributeError` car le nom correct de l'attribut est `shares`.

2. Après avoir ajouté ces méthodes de test, enregistrez le fichier `teststock.py`. Ensuite, exécutez tous les tests en utilisant la commande suivante dans votre terminal :

```bash
python3 teststock.py
```

Si tout fonctionne correctement, vous devriez voir une sortie indiquant que les 12 tests ont réussi. La sortie ressemblera à ceci :

```
............
----------------------------------------------------------------------
Ran 12 tests in 0.002s

OK
```

Les douze points représentent tous les tests que vous avez écrits jusqu'à présent. Il y avait 7 tests à l'étape précédente, et nous venons d'en ajouter 5 de nouveaux. Cette sortie montre que votre code gère les exceptions comme prévu, ce qui est un excellent signe d'un programme bien testé.
