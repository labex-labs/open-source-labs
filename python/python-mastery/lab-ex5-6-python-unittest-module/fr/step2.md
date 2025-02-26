# Tests unitaires

En utilisant le code de `teststock.py` comme guide, étendez la classe `TestStock` avec des tests pour les points suivants :

- Vérifiez que vous pouvez créer une instance de `Stock` en utilisant des arguments nommés tels que `Stock(name='GOOG',shares=100,price=490.1)`.
- Testez que la propriété `cost` renvoie une valeur correcte.
- Testez que la méthode `sell()` met à jour correctement le nombre d'actions.
- Testez que la méthode de classe `from_row()` crée une nouvelle instance à partir de données valides.
- Testez que la méthode `__repr__()` crée une chaîne de représentation appropriée.
- Testez la méthode d'opérateur de comparaison `__eq__()`
