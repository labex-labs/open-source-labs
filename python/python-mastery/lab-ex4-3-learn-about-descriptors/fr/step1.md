# Comprendre le protocole des descripteurs

Dans cette étape, nous allons apprendre comment les descripteurs (descriptors) fonctionnent en Python en créant une simple classe `Stock`. Les descripteurs en Python sont une fonctionnalité puissante qui vous permet de personnaliser la manière dont les attributs sont accédés, définis et supprimés. Le protocole des descripteurs se compose de trois méthodes spéciales : `__get__()`, `__set__()` et `__delete__()`. Ces méthodes définissent le comportement du descripteur lorsque l'attribut est accédé, reçoit une valeur ou est supprimé, respectivement.

Tout d'abord, nous devons créer un nouveau fichier appelé `stock.py` dans le répertoire du projet. Ce fichier contiendra notre classe `Stock`. Voici le code que vous devez placer dans le fichier `stock.py` :

```python
# stock.py

class Stock:
    __slots__ = ['_name', '_shares', '_price']

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected an integer')
        if value < 0:
            raise ValueError('Expected a positive value')
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Expected a number')
        if value < 0:
            raise ValueError('Expected a positive value')
        self._price = value

    def cost(self):
        return self.shares * self.price

    def sell(self, amount):
        self.shares -= amount

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
```

Dans cette classe `Stock`, nous utilisons le décorateur `property` pour définir les méthodes getter et setter pour les attributs `name`, `shares` et `price`. Ces méthodes getter et setter agissent comme des descripteurs, ce qui signifie qu'elles contrôlent la manière dont ces attributs sont accédés et définis. Par exemple, les méthodes setter valident les valeurs d'entrée pour s'assurer qu'elles sont du bon type et dans une plage acceptable.

Maintenant que notre fichier `stock.py` est prêt, ouvrons un interpréteur Python pour expérimenter avec la classe `Stock` et voir comment les descripteurs fonctionnent en pratique. Pour ce faire, ouvrez votre terminal et exécutez les commandes suivantes :

```bash
cd ~/project
python3 -i stock.py
```

L'option `-i` dans la commande `python3` indique à Python de démarrer un interpréteur interactif après avoir exécuté le fichier `stock.py`. De cette façon, nous pouvons interagir directement avec la classe `Stock` que nous venons de définir.

Dans l'interpréteur Python, créons un objet `Stock` et essayons d'accéder à ses attributs. Voici comment vous pouvez le faire :

```python
s = Stock('GOOG', 100, 490.10)
s.name      # Should return 'GOOG'
s.shares    # Should return 100
```

Lorsque vous accédez aux attributs `name` et `shares` de l'objet `s`, Python utilise en réalité la méthode `__get__` du descripteur en arrière-plan. Les décorateurs `property` de notre classe sont implémentés à l'aide de descripteurs, ce qui signifie qu'ils gèrent l'accès et l'affectation des attributs de manière contrôlée.

Regardons de plus près le dictionnaire de classe pour voir les objets descripteurs. Le dictionnaire de classe contient tous les attributs et méthodes définis dans la classe. Vous pouvez afficher les clés du dictionnaire de classe en utilisant le code suivant :

```python
Stock.__dict__.keys()
```

Vous devriez voir une sortie similaire à ceci :

```
dict_keys(['__module__', '__slots__', '__init__', 'name', '_name', 'shares', '_shares', 'price', '_price', 'cost', 'sell', '__repr__', '__doc__'])
```

Les clés `name`, `shares` et `price` représentent les objets descripteurs créés par les décorateurs `property`.

Maintenant, examinons comment les descripteurs fonctionnent en appelant manuellement leurs méthodes. Nous utiliserons le descripteur `shares` comme exemple. Voici comment vous pouvez le faire :

```python
# Get the descriptor object for 'shares'
q = Stock.__dict__['shares']

# Use the __get__ method to retrieve the value
q.__get__(s, Stock)  # Should return 100

# Use the __set__ method to set a new value
q.__set__(s, 75)
s.shares  # Should now be 75

# Try to set an invalid value
try:
    q.__set__(s, '75')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")
```

Lorsque vous accédez à un attribut comme `s.shares`, Python appelle la méthode `__get__` du descripteur pour récupérer la valeur. Lorsque vous assignez une valeur comme `s.shares = 75`, Python appelle la méthode `__set__` du descripteur. Le descripteur peut alors valider les données et lever des erreurs si la valeur d'entrée n'est pas valide.

Une fois que vous avez terminé d'expérimenter avec la classe `Stock` et les descripteurs, vous pouvez quitter l'interpréteur Python en exécutant la commande suivante :

```python
exit()
```
