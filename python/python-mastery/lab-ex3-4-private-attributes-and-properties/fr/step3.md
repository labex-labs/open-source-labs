# Mise en œuvre de la validation des propriétés

Les propriétés (properties) en Python sont une fonctionnalité puissante. Elles vous permettent non seulement d'accéder à des valeurs calculées comme si elles étaient des attributs normaux, mais elles vous donnent également le contrôle sur la façon dont ces valeurs d'attributs sont récupérées, définies et supprimées. Ce contrôle est extrêmement utile lorsque vous avez besoin d'ajouter une validation à vos attributs. La validation garantit que les valeurs assignées aux attributs répondent à des critères spécifiques, ce qui contribue à maintenir l'intégrité de vos données.

Dans notre classe `Stock`, nous avons deux attributs importants : `shares` et `price`. Nous voulons nous assurer que `shares` est un entier non négatif et que `price` est un nombre à virgule flottante non négatif. Pour réaliser cette validation, nous allons utiliser des décorateurs de propriétés ainsi que des accesseurs (getters) et des mutateurs (setters).

## Instructions :

1. Tout d'abord, vous devez ouvrir le fichier `stock.py` dans l'éditeur. C'est là que nous allons apporter toutes les modifications à notre classe `Stock`. Utilisez la commande suivante dans le terminal :

   ```bash
   code /home/labex/project/stock.py
   ```

2. En Python, nous pouvons utiliser des attributs privés pour stocker les valeurs réelles de nos variables de classe. Les attributs privés sont indiqués par un trait de soulignement au début. Ajoutez les attributs privés `_shares` et `_price` à la classe `Stock` et modifiez le constructeur pour les utiliser. Le constructeur est la méthode qui est appelée lorsque vous créez une nouvelle instance de la classe. Voici comment faire :

   ```python
   def __init__(self, name, shares, price):
       self.name = name
       self._shares = shares  # Using private attribute
       self._price = price    # Using private attribute
   ```

3. Maintenant, nous allons définir des propriétés pour `shares` et `price` avec une validation appropriée. Les propriétés sont définies en utilisant le décorateur `@property` pour la méthode accesseur (getter) et le décorateur `@<property_name>.setter` pour la méthode mutateur (setter). La méthode accesseur est utilisée pour récupérer la valeur de l'attribut, et la méthode mutateur est utilisée pour définir la valeur. Voici le code pour ajouter les définitions de propriétés avec validation :

   ```python
   @property
   def shares(self):
       return self._shares

   @shares.setter
   def shares(self, value):
       if not isinstance(value, int):
           raise TypeError("Expected integer")
       if value < 0:
           raise ValueError("shares must be >= 0")
       self._shares = value

   @property
   def price(self):
       return self._price

   @price.setter
   def price(self, value):
       if not isinstance(value, float):
           raise TypeError("Expected float")
       if value < 0:
           raise ValueError("price must be >= 0")
       self._price = value
   ```

4. Mettez à jour le constructeur pour utiliser les mutateurs de propriétés pour la validation. De cette façon, chaque fois qu'une nouvelle instance de la classe `Stock` est créée, les valeurs de `shares` et `price` seront automatiquement validées. Voici le constructeur mis à jour :

   ```python
   def __init__(self, name, shares, price):
       self.name = name
       self.shares = shares  # Using property setter
       self.price = price    # Using property setter
   ```

5. Après avoir apporté toutes ces modifications, enregistrez le fichier `stock.py`. Cela garantit que vos modifications sont conservées.

6. Pour vérifier que notre validation fonctionne correctement, nous allons créer un script de test. Ouvrez un nouveau fichier nommé `test_validation.py` dans l'éditeur en utilisant la commande suivante :

   ```bash
   code /home/labex/project/test_validation.py
   ```

7. Ajoutez le code suivant au fichier `test_validation.py`. Ce code crée une instance valide de `Stock`, puis essaie de mettre à jour les attributs `shares` et `price` avec des valeurs valides et invalides. Il affiche également les résultats et tous les messages d'erreur qui se produisent.

   ```python
   from stock import Stock

   # Create a valid stock instance
   s = Stock('GOOG', 100, 490.10)
   print(f"Initial: Name={s.name}, Shares={s.shares}, Price={s.price}, Cost={s.cost}")

   # Test valid updates
   try:
       s.shares = 50  # Valid update
       print(f"After setting shares=50: Shares={s.shares}, Cost={s.cost}")
   except Exception as e:
       print(f"Error setting shares=50: {e}")

   try:
       s.price = 123.45  # Valid update
       print(f"After setting price=123.45: Price={s.price}, Cost={s.cost}")
   except Exception as e:
       print(f"Error setting price=123.45: {e}")

   # Test invalid updates
   try:
       s.shares = "50"  # Invalid type (string)
       print("This line should not execute")
   except Exception as e:
       print(f"Error setting shares='50': {e}")

   try:
       s.shares = -10  # Invalid value (negative)
       print("This line should not execute")
   except Exception as e:
       print(f"Error setting shares=-10: {e}")

   try:
       s.price = "123.45"  # Invalid type (string)
       print("This line should not execute")
   except Exception as e:
       print(f"Error setting price='123.45': {e}")

   try:
       s.price = -10.0  # Invalid value (negative)
       print("This line should not execute")
   except Exception as e:
       print(f"Error setting price=-10.0: {e}")
   ```

8. Enfin, exécutez le script de test en utilisant la commande suivante dans le terminal :
   ```bash
   python /home/labex/project/test_validation.py
   ```

Vous devriez voir une sortie qui montre des mises à jour valides réussies et des messages d'erreur appropriés pour les mises à jour invalides. Cela confirme que notre validation de propriétés fonctionne comme prévu.
