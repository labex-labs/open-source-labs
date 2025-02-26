# Les directions de l'héritage

Python a deux "directions" différentes d'héritage. La première se trouve dans le concept d'"héritage simple" où une série de classes hérite d'un seul parent. Par exemple, essayez cet exemple :

```python
>>> class A:
        def spam(self):
            print('A.spam')

>>> class B(A):
        def spam(self):
            print('B.spam')
            super().spam()

>>> class C(B):
        def spam(self):
            print('C.spam')
            super().spam()


>>> C.__mro__
(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
>>> c = C()
>>> c.spam()
C.spam
B.spam
A.spam
>>>
```

Observez que l'attribut `__mro__` de la classe `C` encode tous ses ancêtres dans l'ordre. Lorsque vous appelez la méthode `spam()`, elle parcourt la hiérarchie classe par classe selon le MRO.

Avec l'héritage multiple, vous obtenez un autre type d'héritage qui permet de composer différentes classes ensemble. Essayez cet exemple :

```python
>>> class Base:
        def spam(self):
            print('Base.spam')

>>> class X(Base):
        def spam(self):
            print('X.spam')
            super().spam()

>>> class Y(Base):
        def spam(self):
            print('Y.spam')
            super().spam()

>>> class Z(Base):
        def spam(self):
            print('Z.spam')
            super().spam()

>>>
```

Remarquez que toutes les classes ci-dessus héritent d'un parent commun `Base`. Cependant, les classes `X`, `Y` et `Z` ne sont pas directement liées les unes aux autres (il n'y a pas de chaîne d'héritage reliant ces classes ensemble).

Cependant, observez ce qui se passe avec l'héritage multiple :

```python
>>> class M(X,Y,Z):
        pass

>>> M.__mro__
(<class '__main__.M'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class '__main__.Base'>, <class 'object'>)
>>> m = M()
>>> m.spam()
X.spam
Y.spam
Z.spam
Base.spam
>>>
```

Ici, vous voyez toutes les classes s'empiler dans l'ordre fourni par la sous-classe. Supposons que la sous-classe réorganise l'ordre des classes :

```python
>>> class N(Z,Y,X):
        pass

>>> N.__mro__
(<class '__main__.N'>, <class '__main__.Z'>, <class '__main__.Y'>, <class '__main__.X'>, <class '__main__.Base'>, <class 'object'>)
>>> n = N()
>>> n.spam()
Z.spam
Y.spam
X.spam
Base.spam
>>>
```

Ici, vous voyez l'ordre des parents inversé. Attention attentivement à ce que `super()` fait dans les deux cas. Elle ne délègue pas au parent immédiat de chaque classe - au lieu de cela, elle passe à la classe suivante du MRO. Pas seulement ça, l'ordre exact est contrôlé par l'enfant. C'est assez étrange.

Remarquez également que le parent commun `Base` sert à terminer la chaîne d'opérations `super()`. Plus précisément, la méthode `Base.spam()` n'appelle pas d'autres méthodes. Elle apparaît également à la fin du MRO car elle est la parent de toutes les classes composées ensemble.
