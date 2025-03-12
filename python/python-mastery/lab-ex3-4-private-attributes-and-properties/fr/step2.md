# Conversion de méthodes en propriétés

En Python, les propriétés (properties) sont une fonctionnalité puissante qui vous permet d'accéder à des valeurs calculées de manière similaire à l'accès aux attributs. Normalement, lorsque vous souhaitez obtenir une valeur à partir d'une méthode, vous devez utiliser des parenthèses pour appeler cette méthode. Cependant, les propriétés éliminent le besoin de ces parenthèses, rendant votre code plus propre et plus cohérent avec la façon dont vous accédez aux attributs normaux.

Regardons notre classe `Stock` actuelle. Elle a une méthode `cost()` qui calcule le coût total des actions. Cette méthode multiplie le nombre d'actions par le prix unitaire pour nous donner le coût total. Voici à quoi ressemble la méthode `cost()` :

```python
def cost(self):
    return self.shares * self.price
```

Pour obtenir la valeur du coût en utilisant cette méthode, nous devons l'appeler avec des parenthèses, comme ceci :

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost())  # Calls the method
```

Mais nous pouvons améliorer notre code. En convertissant la méthode `cost()` en une propriété, nous pouvons accéder à la valeur du coût tout comme nous accédons aux autres attributs, sans utiliser de parenthèses. Voici à quoi cela ressemblerait :

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost)  # Accesses the property
```

## Instructions :

1. Tout d'abord, nous devons ouvrir le fichier `stock.py` dans l'éditeur. C'est là que la classe `Stock` est définie, et nous allons apporter des modifications à cette classe. Utilisez la commande suivante dans le terminal :

   ```bash
   code /home/labex/project/stock.py
   ```

2. À l'intérieur du fichier `stock.py`, nous allons remplacer la méthode `cost()` par une propriété. Nous allons utiliser le décorateur `@property` pour cela. Le décorateur `@property` indique à Python que la méthode suivante doit être traitée comme une propriété. Remplacez la méthode `cost()` par le code suivant :

   ```python
   @property
   def cost(self):
       return self.shares * self.price
   ```

3. Après avoir apporté les modifications, enregistrez le fichier `stock.py`. Cela garantit que nos modifications sont enregistrées et peuvent être utilisées plus tard.

4. Maintenant, nous devons créer un simple script Python pour tester notre nouvelle propriété. Ouvrez un nouveau fichier nommé `test_property.py` dans l'éditeur en utilisant la commande suivante :

   ```bash
   code /home/labex/project/test_property.py
   ```

5. Dans le fichier `test_property.py`, nous allons ajouter du code pour créer une instance de `Stock` et accéder à la propriété `cost`. Voici le code que vous devriez ajouter :

   ```python
   from stock import Stock

   # Create a stock instance
   s = Stock('GOOG', 100, 490.10)

   # Access cost as a property (no parentheses)
   print(f"Stock: {s.name}")
   print(f"Shares: {s.shares}")
   print(f"Price: {s.price}")
   print(f"Cost: {s.cost}")  # Using the property
   ```

6. Enfin, exécutez le script de test pour voir si notre propriété fonctionne comme prévu. Utilisez la commande suivante dans le terminal :
   ```bash
   python /home/labex/project/test_property.py
   ```

Vous devriez voir une sortie similaire à :

```
Stock: GOOG
Shares: 100
Price: 490.1
Cost: 49010.0
```

Remarquez comment nous pouvons maintenant accéder à `cost` comme à un attribut (sans parenthèses), rendant notre code plus cohérent avec la façon dont nous accédons aux autres attributs comme `name`, `shares` et `price`. Cela rend notre code plus facile à lire et à maintenir.
