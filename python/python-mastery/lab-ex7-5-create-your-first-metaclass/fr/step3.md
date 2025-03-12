# Utiliser votre métaclasse

Maintenant, nous allons créer une classe qui utilise notre métaclasse par héritage. Cela nous aidera à comprendre comment la métaclasse est appelée lorsque la classe est définie.

Une métaclasse en Python est une classe qui crée d'autres classes. Lorsque vous définissez une classe, Python utilise une métaclasse pour construire l'objet de cette classe. En utilisant l'héritage, nous pouvons spécifier quelle métaclasse une classe doit utiliser.

1. Ouvrez le fichier `mymeta.py` et ajoutez le code suivant à la fin du fichier :

```python
class Stock(myobject):
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

Ici, nous définissons une classe `Stock` qui hérite de `myobject`. La méthode `__init__` est une méthode spéciale dans les classes Python. Elle est appelée lorsque un objet de la classe est créé et est utilisée pour initialiser les attributs de l'objet. La méthode `cost` calcule le coût total des actions, et la méthode `sell` réduit le nombre d'actions.

2. Enregistrez le fichier en appuyant sur Ctrl+S. Enregistrer le fichier garantit que les modifications que vous avez apportées sont enregistrées et peuvent être exécutées plus tard.

3. Maintenant, exécutons le fichier pour voir ce qui se passe. Ouvrez un terminal dans le WebIDE et exécutez :

```bash
cd /home/labex/project
python3 mymeta.py
```

La commande `cd` change le répertoire de travail actuel en `/home/labex/project`, et `python3 mymeta.py` exécute le script Python `mymeta.py`.

Vous devriez voir une sortie similaire à ceci :

```
Creating class : myobject
Base classes   : ()
Attributes     : ['__module__', '__qualname__', '__doc__']
Creating class : Stock
Base classes   : (<class '__main__.myobject'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'cost', 'sell', '__doc__']
```

Cette sortie montre que notre métaclasse est invoquée lorsque les classes `myobject` et `Stock` sont créées. Remarquez comment :

- Pour `Stock`, les classes de base incluent `myobject` car `Stock` hérite de `myobject`.
- La liste des attributs inclut toutes les méthodes que nous avons définies (`__init__`, `cost`, `sell`) ainsi que certains attributs par défaut.

4. Interagissons avec notre classe `Stock`. Créez un nouveau fichier nommé `test_stock.py` avec le contenu suivant :

```python
# test_stock.py
from mymeta import Stock

# Create a new Stock instance
apple = Stock("AAPL", 100, 154.50)

# Use the methods
print(f"Stock: {apple.name}, Shares: {apple.shares}, Price: ${apple.price}")
print(f"Total cost: ${apple.cost()}")

# Sell some shares
apple.sell(10)
print(f"After selling 10 shares: {apple.shares} shares remaining")
print(f"Updated cost: ${apple.cost()}")
```

Dans ce code, nous importons la classe `Stock` du module `mymeta`. Ensuite, nous créons une instance de la classe `Stock` nommée `apple`. Nous utilisons les méthodes de la classe `Stock` pour afficher des informations sur les actions, calculer le coût total, vendre quelques actions, puis afficher les informations mises à jour.

5. Exécutez ce fichier pour tester notre classe `Stock` :

```bash
python3 test_stock.py
```

Vous devriez voir une sortie comme celle - ci :

```
Creating class : myobject
Base classes   : ()
Attributes     : ['__module__', '__qualname__', '__doc__']
Creating class : Stock
Base classes   : (<class 'mymeta.myobject'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'cost', 'sell', '__doc__']
Stock: AAPL, Shares: 100, Price: $154.5
Total cost: $15450.0
After selling 10 shares: 90 shares remaining
Updated cost: $13905.0
```

Remarquez que les informations de notre métaclasse sont affichées en premier, suivies de la sortie de notre script de test. Cela s'explique par le fait que la métaclasse est invoquée lorsque la classe est définie, ce qui se produit avant l'exécution du code dans le script de test.
