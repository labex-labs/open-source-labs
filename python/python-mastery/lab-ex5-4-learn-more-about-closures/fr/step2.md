# Les closures comme un générateur de code

Dans l'exercice 4.3, vous avez développé une collection de classes de descripteurs qui permettent de vérifier le type des attributs d'un objet. Par exemple :

```python

class Stock:
    name = String()
    shares = Integer()
    price = Float()
```

Ce genre de chose peut également être implémenté à l'aide de closures. Créez un fichier `typedproperty.py` et mettez le code suivant dedans :

```python
# typedproperty.py

def typedproperty(name, expected_type):
    private_name = '_' + name

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, val)

    return value
```

Cela semble assez étrange, mais la fonction est en fait un générateur de code. Vous l'utiliseriez dans une définition de classe comme ceci :

```python
from typedproperty import typedproperty

class Stock:
    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Vérifiez que cette classe effectue la vérification de type de la même manière que le code du descripteur.

Ajoutez les fonctions `String()`, `Integer()` et `Float()` au fichier `typedproperty.py` de sorte que vous puissiez écrire le code suivant :

```python
from typedproperty import String, Integer, Float

class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```
