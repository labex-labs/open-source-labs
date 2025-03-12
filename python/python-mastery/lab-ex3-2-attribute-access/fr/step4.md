# Comprendre les méthodes liées (bound methods) en Python

En Python, les méthodes sont un type spécial d'attributs que vous pouvez appeler. Lorsque vous accédez à une méthode via un objet, vous obtenez ce que l'on appelle une "méthode liée" (bound method). Une méthode liée est essentiellement une méthode qui est associée à un objet spécifique. Cela signifie qu'elle a accès aux données de l'objet et peut opérer sur elles.

## Accéder aux méthodes en tant qu'attributs

Commençons à explorer les méthodes liées en utilisant notre classe `Stock`. Tout d'abord, voyons comment accéder à une méthode en tant qu'attribut d'un objet.

```python
# Open a Python interactive shell
python3

# Import the Stock class and create a stock object
from stock import Stock
s = Stock('GOOG', 100, 490.10)

# Access the cost method without calling it
cost_method = s.cost
print(cost_method)  # Output: <bound method Stock.cost of <stock.Stock object at 0x...>>

# Call the method
result = cost_method()
print(result)  # Output: 49010.0

# You can also do this in one step
print(s.cost())  # Output: 49010.0
```

Dans le code ci-dessus, nous importons d'abord la classe `Stock` et créons une instance de celle-ci. Ensuite, nous accédons à la méthode `cost` de l'objet `s` sans l'appeler réellement. Cela nous donne une méthode liée. Lorsque nous appelons cette méthode liée, elle calcule le coût en fonction des données de l'objet. Vous pouvez également appeler directement la méthode sur l'objet en une seule étape.

## Utiliser `getattr()` avec les méthodes

Une autre façon d'accéder aux méthodes est d'utiliser la fonction `getattr()`. Cette fonction vous permet d'obtenir un attribut d'un objet par son nom.

```python
# Get the cost method using getattr
cost_method = getattr(s, 'cost')
print(cost_method)  # Output: <bound method Stock.cost of <stock.Stock object at 0x...>>

# Call the method
result = cost_method()
print(result)  # Output: 49010.0

# Get and call in one step
result = getattr(s, 'cost')()
print(result)  # Output: 49010.0
```

Ici, nous utilisons `getattr()` pour obtenir la méthode `cost` de l'objet `s`. Tout comme précédemment, nous pouvons appeler la méthode liée pour obtenir le résultat. Et vous pouvez même obtenir et appeler la méthode en une seule ligne.

## La méthode liée et son objet

Une méthode liée garde toujours une référence à l'objet à partir duquel elle a été accédée. Cela signifie que même si vous stockez la méthode dans une variable, elle sait toujours à quel objet elle appartient et peut accéder aux données de cet objet.

```python
# Store the cost method in a variable
c = s.cost

# Call the method
print(c())  # Output: 49010.0

# Change the object's state
s.shares = 75

# Call the method again - it sees the updated state
print(c())  # Output: 36757.5
```

Dans cet exemple, nous stockons la méthode `cost` dans une variable `c`. Lorsque nous appelons `c()`, elle calcule le coût en fonction des données actuelles de l'objet. Ensuite, nous changeons l'attribut `shares` de l'objet `s`. Lorsque nous appelons `c()` à nouveau, elle utilise les données mises à jour pour calculer le nouveau coût.

## Explorer les internals de la méthode liée

Une méthode liée a deux attributs importants qui nous donnent plus d'informations sur elle.

- `__self__` : Cet attribut fait référence à l'objet auquel la méthode est liée.
- `__func__` : Cet attribut est l'objet fonction réel qui représente la méthode.

```python
# Get the cost method
c = s.cost

# Examine the bound method attributes
print(c.__self__)  # Output: <stock.Stock object at 0x...>
print(c.__func__)  # Output: <function Stock.cost at 0x...>

# You can manually call the function with the object
print(c.__func__(c.__self__))  # Output: 36757.5 (same as c())
```

Ici, nous accédons aux attributs `__self__` et `__func__` de la méthode liée `c`. Nous pouvons voir que `__self__` est l'objet `s`, et `__func__` est la fonction `cost`. Nous pouvons même appeler manuellement la fonction en passant l'objet en argument, et cela nous donne le même résultat qu'en appelant directement la méthode liée.

## Exemple avec une méthode qui prend des arguments

Voyons comment les méthodes liées fonctionnent avec une méthode qui prend des arguments, comme la méthode `sell()`.

```python
# Get the sell method
sell_method = s.sell

# Examine the method
print(sell_method)  # Output: <bound method Stock.sell of <stock.Stock object at 0x...>>

# Call the method with an argument
sell_method(25)
print(s.shares)  # Output: 50

# Call the method manually using __func__ and __self__
sell_method.__func__(sell_method.__self__, 10)
print(s.shares)  # Output: 40
```

Dans cet exemple, nous obtenons la méthode `sell` sous forme de méthode liée. Lorsque nous l'appelons avec un argument, elle met à jour l'attribut `shares` de l'objet `s`. Nous pouvons également appeler manuellement la méthode en utilisant les attributs `__func__` et `__self__`, en passant également l'argument.

Comprendre les méthodes liées vous aide à comprendre le fonctionnement interne du système d'objets de Python, ce qui peut être utile pour le débogage, la métaprogrammation et la création de modèles de programmation avancés.
