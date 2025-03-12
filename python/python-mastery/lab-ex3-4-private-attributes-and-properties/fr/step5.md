# Réconciliation de la validation de type avec les variables de classe

Dans notre parcours de programmation Python, nous avons créé une classe `Stock`. Actuellement, cette classe dispose de deux méthodes différentes pour gérer les types de données. Comprendre ces mécanismes est crucial car cela nous aide à mieux gérer et organiser notre code.

Le premier mécanisme est la variable de classe `_types`. Cette variable est utilisée pour convertir les données provenant de lignes. Lorsque nous recevons des données au format ligne, la variable `_types` nous aide à transformer ces données en types appropriés pour notre classe `Stock`.

Le deuxième mécanisme est constitué des mutateurs (setters) de propriétés. Ces mutateurs appliquent la vérification de type. Chaque fois que nous essayons de définir une valeur pour une propriété dans notre classe `Stock`, les mutateurs de propriétés s'assurent que la valeur est du bon type.

Cependant, avoir deux mécanismes distincts peut rendre notre classe difficile à maintenir. Pour résoudre ce problème, nous devons réconcilier ces deux mécanismes afin qu'ils utilisent les mêmes informations de type. De cette façon, nous assurons la cohérence de notre classe, et elle devient plus fiable lors de la création de sous - classes.

## Instructions :

1. Tout d'abord, nous devons ouvrir le fichier `stock.py` dans l'éditeur. Ce fichier contient le code de notre classe `Stock`. Pour l'ouvrir, exécutez la commande suivante dans le terminal :

   ```bash
   code /home/labex/project/stock.py
   ```

2. Maintenant, nous allons modifier les mutateurs de propriétés dans le fichier `stock.py`. Nous voulons qu'ils utilisent les types définis dans la variable de classe `_types`. Cela garantit que la vérification de type dans les mutateurs de propriétés est cohérente avec la conversion de type effectuée par la variable `_types`. Voici comment nous modifions les mutateurs de propriétés :

   ```python
   @property
   def shares(self):
       return self._shares

   @shares.setter
   def shares(self, value):
       if not isinstance(value, self._types[1]):
           raise TypeError(f"Expected {self._types[1].__name__}")
       if value < 0:
           raise ValueError("shares must be >= 0")
       self._shares = value

   @property
   def price(self):
       return self._price

   @price.setter
   def price(self, value):
       if not isinstance(value, self._types[2]):
           raise TypeError(f"Expected {self._types[2].__name__}")
       if value < 0:
           raise ValueError("price must be >= 0")
       self._price = value
   ```

3. Après avoir apporté ces modifications, enregistrez le fichier `stock.py`. Enregistrer le fichier garantit que nos modifications sont conservées.

4. Ensuite, nous allons créer un script de test pour vérifier que la création de sous - classes avec différents types fonctionne comme prévu. Pour créer ce script, exécutez la commande suivante dans le terminal :

   ```bash
   code /home/labex/project/test_subclass.py
   ```

5. Maintenant, ajoutez le code suivant au fichier `test_subclass.py`. Ce code crée une sous - classe de la classe `Stock` avec différents types et teste à la fois la classe de base et la sous - classe.

   ```python
   from stock import Stock
   from decimal import Decimal

   # Create a subclass with different types
   class DStock(Stock):
       _types = (str, int, Decimal)

   # Test the base class
   s = Stock('GOOG', 100, 490.10)
   print(f"Stock: {s.name}, Shares: {s.shares}, Price: {s.price}, Cost: {s.cost}")

   # Test valid update with float
   try:
       s.price = 500.25
       print(f"Updated Stock price: {s.price}, Cost: {s.cost}")
   except Exception as e:
       print(f"Error updating Stock price: {e}")

   # Test the subclass with Decimal
   ds = DStock('AAPL', 50, Decimal('142.50'))
   print(f"DStock: {ds.name}, Shares: {ds.shares}, Price: {ds.price}, Cost: {ds.cost}")

   # Test invalid update with float (should require Decimal)
   try:
       ds.price = 150.75
       print(f"Updated DStock price: {ds.price}")
   except Exception as e:
       print(f"Error updating DStock price: {e}")

   # Test valid update with Decimal
   try:
       ds.price = Decimal('155.25')
       print(f"Updated DStock price: {ds.price}, Cost: {ds.cost}")
   except Exception as e:
       print(f"Error updating DStock price: {e}")
   ```

6. Enfin, exécutez le script de test pour voir les résultats. Exécutez la commande suivante dans le terminal :

   ```bash
   python /home/labex/project/test_subclass.py
   ```

Lorsque vous exécutez le script de test, vous devriez constater que la classe de base `Stock` accepte les valeurs flottantes pour le prix, tandis que la sous - classe `DStock` exige des valeurs `Decimal`. Cela montre que notre réconciliation de type a fonctionné comme prévu.

### Discussion

En réconciliant les informations de type dans notre classe `Stock`, nous avons rendu la classe plus cohérente. Maintenant, les mutateurs de propriétés utilisent les mêmes informations de type que la méthode `from_row`. Cette cohérence rend la classe plus facile à maintenir et à étendre, en particulier lors de la création de sous - classes.

Bien que notre implémentation actuelle de la classe `Stock` puisse sembler complexe pour un concept simple, elle démontre des techniques Python importantes pour l'encapsulation et la sécurité de type. Dans les applications du monde réel, vous voudrez peut - être utiliser des outils plus avancés comme les dataclasses ou des bibliothèques tierces pour simplifier ce type d'implémentation. Ces outils peuvent rendre votre code plus concis et plus facile à gérer.
