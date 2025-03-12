# Élargissement de vos cas de test

Maintenant que vous avez créé un cas de test de base, il est temps d'élargir votre champ de test. Ajouter plus de tests vous aidera à couvrir la fonctionnalité restante de la classe `Stock`. De cette façon, vous pouvez vous assurer que tous les aspects de la classe fonctionnent comme prévu. Nous allons modifier la classe `TestStock` pour inclure des tests pour plusieurs méthodes et propriétés.

1. Ouvrez le fichier `teststock.py`. À l'intérieur de la classe `TestStock`, nous allons ajouter quelques nouvelles méthodes de test. Ces méthodes testeront différentes parties de la classe `Stock`. Voici le code que vous devez ajouter :

```python
def test_create_keyword_args(self):
    s = stock.Stock(name='GOOG', shares=100, price=490.1)
    self.assertEqual(s.name, 'GOOG')
    self.assertEqual(s.shares, 100)
    self.assertEqual(s.price, 490.1)

def test_cost(self):
    s = stock.Stock('GOOG', 100, 490.1)
    self.assertEqual(s.cost, 49010.0)

def test_sell(self):
    s = stock.Stock('GOOG', 100, 490.1)
    s.sell(20)
    self.assertEqual(s.shares, 80)

def test_from_row(self):
    row = ['GOOG', '100', '490.1']
    s = stock.Stock.from_row(row)
    self.assertEqual(s.name, 'GOOG')
    self.assertEqual(s.shares, 100)
    self.assertEqual(s.price, 490.1)

def test_repr(self):
    s = stock.Stock('GOOG', 100, 490.1)
    self.assertEqual(repr(s), "Stock('GOOG', 100, 490.1)")

def test_eq(self):
    s1 = stock.Stock('GOOG', 100, 490.1)
    s2 = stock.Stock('GOOG', 100, 490.1)
    self.assertEqual(s1, s2)
```

Examinons de plus près ce que chaque test fait :

- `test_create_keyword_args` : Ce test vérifie si vous pouvez créer un objet `Stock` en utilisant des arguments nommés (keyword arguments). Il vérifie que les attributs de l'objet sont correctement définis.
- `test_cost` : Ce test vérifie si la propriété `cost` d'un objet `Stock` renvoie la bonne valeur, qui est calculée comme le nombre d'actions multiplié par le prix.
- `test_sell` : Ce test vérifie si la méthode `sell()` d'un objet `Stock` met correctement à jour le nombre d'actions après avoir vendu certaines d'entre elles.
- `test_from_row` : Ce test vérifie si la méthode de classe `from_row()` peut créer une nouvelle instance de `Stock` à partir d'une ligne de données.
- `test_repr` : Ce test vérifie si la méthode `__repr__()` d'un objet `Stock` renvoie la représentation sous forme de chaîne de caractères attendue.
- `test_eq` : Ce test vérifie si la méthode `__eq__()` compare correctement deux objets `Stock` pour voir s'ils sont égaux.

2. Après avoir ajouté ces méthodes de test, enregistrez le fichier `teststock.py`. Ensuite, exécutez les tests à nouveau en utilisant la commande suivante dans votre terminal :

```bash
python3 teststock.py
```

Si tous les tests réussissent, vous devriez voir une sortie comme celle - ci :

```
......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```

Les sept points dans la sortie représentent chaque test. Chaque point indique qu'un test a réussi avec succès. Donc, si vous voyez sept points, cela signifie que les sept tests ont réussi.
