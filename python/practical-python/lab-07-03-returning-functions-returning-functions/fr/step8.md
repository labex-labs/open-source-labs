# Exercice 7.8 : Simplifier les appels de fonction

Dans l'exemple ci-dessus, les utilisateurs pourraient trouver des appels tels que `typedproperty('shares', int)` un peu verbeux à taper - surtout s'ils sont répétés fréquemment. Ajoutez les définitions suivantes au fichier `typedproperty.py` :

```python
String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)
```

Maintenant, réécrivez la classe `Stock` pour utiliser ces fonctions à la place :

```python
class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Ah, c'est un peu mieux. Le principal enseignement ici est que les closures et les `lambda` peuvent souvent être utilisés pour simplifier le code et éliminer la répétition ennuyeuse. Cela est souvent bénéfique.
