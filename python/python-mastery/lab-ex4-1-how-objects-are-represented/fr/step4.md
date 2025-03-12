# Comprendre la relation entre les classes et les instances

Maintenant, nous allons explorer comment les classes et les instances sont liées en Python, et comment la recherche de méthodes fonctionne. C'est un concept important car il vous aide à comprendre comment Python trouve et utilise les méthodes et les attributs lorsque vous travaillez avec des objets.

Tout d'abord, vérifions à quelle classe appartiennent nos instances. Savoir la classe d'une instance est crucial car cela nous indique où Python cherchera les méthodes et les attributs liés à cette instance.

```python
>>> goog.__class__
<class '__main__.SimpleStock'>
>>> ibm.__class__
<class '__main__.SimpleStock'>
```

Les deux instances ont une référence vers la classe `SimpleStock`. Cette référence est comme un pointeur que Python utilise lorsqu'il a besoin de rechercher des méthodes. Lorsque vous appelez une méthode sur une instance, Python utilise cette référence pour trouver la définition appropriée de la méthode.

Lorsque vous appelez une méthode sur une instance, Python suit ces étapes :

1. Il cherche l'attribut dans le `__dict__` de l'instance. Le `__dict__` d'une instance est comme une zone de stockage où tous les attributs spécifiques à l'instance sont conservés.
2. S'il n'est pas trouvé, il vérifie le `__dict__` de la classe. Le `__dict__` de la classe stocke tous les attributs et les méthodes qui sont communs à toutes les instances de cette classe.
3. S'il est trouvé dans la classe, il renvoie cet attribut.

Voyons cela en action. Tout d'abord, vérifions que la méthode `cost` n'est pas dans les dictionnaires des instances. Cette étape nous aide à comprendre que la méthode `cost` n'est pas spécifique à chaque instance mais est définie au niveau de la classe.

```python
>>> 'cost' in goog.__dict__
False
>>> 'cost' in ibm.__dict__
False
```

Alors, d'où vient la méthode `cost` ? Vérifions la classe. En regardant le `__dict__` de la classe, nous pouvons découvrir où la méthode `cost` est définie.

```python
>>> SimpleStock.__dict__['cost']
<function SimpleStock.cost at 0x7f...>
```

La méthode est définie dans la classe, pas dans les instances. Lorsque vous appelez `goog.cost()`, Python ne trouve pas `cost` dans `goog.__dict__`, donc il cherche dans `SimpleStock.__dict__` et la trouve là.

Vous pouvez en fait appeler la méthode directement depuis le dictionnaire de la classe, en passant l'instance comme premier argument (qui devient `self`). Cela montre comment Python appelle les méthodes en interne lorsque vous utilisez la syntaxe normale instance.méthode().

```python
>>> SimpleStock.__dict__['cost'](goog)
49010.0
>>> SimpleStock.__dict__['cost'](ibm)
4561.5
```

C'est essentiellement ce que Python fait en coulisse lorsque vous appelez `goog.cost()`.

Maintenant, ajoutons un attribut de classe. Les attributs de classe sont partagés par toutes les instances. Cela signifie que toutes les instances de la classe peuvent accéder à cet attribut, et qu'il n'est stocké qu'une seule fois au niveau de la classe.

```python
>>> SimpleStock.exchange = 'NASDAQ'
>>> goog.exchange
'NASDAQ'
>>> ibm.exchange
'NASDAQ'
```

Les deux instances peuvent accéder à l'attribut `exchange`, mais il n'est pas stocké dans leurs dictionnaires individuels. Vérifions cela en vérifiant les dictionnaires de l'instance et de la classe.

```python
>>> 'exchange' in goog.__dict__
False
>>> 'exchange' in SimpleStock.__dict__
True
>>> SimpleStock.__dict__['exchange']
'NASDAQ'
```

Cela démontre que :

1. Les attributs de classe sont partagés par toutes les instances. Toutes les instances peuvent accéder au même attribut de classe sans avoir leur propre copie.
2. Python vérifie d'abord le dictionnaire de l'instance, puis le dictionnaire de la classe. C'est l'ordre dans lequel Python cherche les attributs lorsque vous essayez de les accéder sur une instance.
3. Les classes servent de dépôt pour les données et les comportements (méthodes) partagés. La classe stocke tous les attributs et les méthodes communs qui peuvent être utilisés par toutes ses instances.

Si nous modifions un attribut d'instance avec le même nom, il masque l'attribut de classe. Cela signifie que lorsque vous accédez à l'attribut sur cette instance, Python utilisera la valeur spécifique à l'instance au lieu de la valeur au niveau de la classe.

```python
>>> ibm.exchange = 'NYSE'
>>> ibm.exchange
'NYSE'
>>> goog.exchange  # Toujours en utilisant l'attribut de classe
'NASDAQ'
>>> ibm.__dict__['exchange']
'NYSE'
```

Maintenant, `ibm` a son propre attribut `exchange` qui masque l'attribut de classe, tandis que `goog` utilise toujours l'attribut de classe.
