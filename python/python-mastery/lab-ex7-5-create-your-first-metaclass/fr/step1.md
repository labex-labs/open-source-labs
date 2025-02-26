# Créez votre première métaclasse

Créez un fichier appelé `mymeta.py` et mettez le code suivant dedans (extrait des diapositives) :

```python
# mymeta.py

class mytype(type):
    @staticmethod
    def __new__(meta, name, bases, __dict__):
        print("Création de la classe :", name)
        print("Classes de base   :", bases)
        print("Attributs     :", list(__dict__))
        return super().__new__(meta, name, bases, __dict__)

class myobject(metaclass=mytype):
    pass
```

Une fois que vous avez fait cela, définissez une classe qui hérite de `myobject` au lieu de `object`. Par exemple :

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

Essayez d'exécuter votre code et de créer des instances de `Stock`. Voir ce qui se passe. Vous devriez voir les instructions `print` de votre `mytype` s'exécuter une fois lorsque la classe `Stock` est définie.

Que se passe-t-il si vous héritez de `Stock`?

```python
class MyStock(Stock):
    pass
```

Vous devriez toujours voir votre métaclasse en action. Les métaclasses sont "statiques" en ce sens qu'elles s'appliquent sur toute une hiérarchie d'héritage.

**Discussion**

Pourquoi voudriez-vous faire quelque chose comme ça? Le principal pouvoir d'une métaclasse est qu'elle donne à un programmeur la possibilité de capturer les détails sur les classes juste avant leur création. Par exemple, dans la méthode `__new__()`, vous recevez tous les détails de base, y compris le nom de la classe, les classes de base et les données des méthodes. Si vous inspectez ces données, vous pouvez effectuer diverses vérifications de diagnostic. Si vous êtes plus audacieux, vous pouvez modifier les données et changer ce qui est placé dans la définition de la classe lors de sa création. Sans dire, il y a de nombreuses opportunités pour des actes diaboliques terribles.
