# Exercice 5.3 : Le rôle des classes

Les définitions qui composent une définition de classe sont partagées par toutes les instances de cette classe. Remarquez que toutes les instances ont un lien vers leur classe associée :

```python
>>> goog.__class__
... regardez la sortie...
>>> ibm.__class__
... regardez la sortie...
>>>
```

Essayez d'appeler une méthode sur les instances :

```python
>>> goog.cost()
49010.0
>>> ibm.cost()
4561.5
>>>
```

Remarquez que le nom 'cost' n'est pas défini dans `goog.__dict__` ni dans `ibm.__dict__`. Au lieu de cela, il est fourni par le dictionnaire de la classe. Essayez ceci :

```python
>>> Stock.__dict__['cost']
... regardez la sortie...
>>>
```

Essayez d'appeler la méthode `cost()` directement via le dictionnaire :

```python
>>> Stock.__dict__['cost'](goog)
49010.0
>>> Stock.__dict__['cost'](ibm)
4561.5
>>>
```

Remarquez comment vous appelez la fonction définie dans la définition de classe et comment l'argument `self` reçoit l'instance.

Essayez d'ajouter un nouvel attribut à la classe `Stock` :

```python
>>> Stock.foo = 42
>>>
```

Remarquez comment ce nouvel attribut apparaît maintenant sur toutes les instances :

```python
>>> goog.foo
42
>>> ibm.foo
42
>>>
```

Cependant, remarquez qu'il n'est pas partie du dictionnaire d'instance :

```python
>>> goog.__dict__
... regardez la sortie et remarquez qu'il n'y a pas d'attribut 'foo'...
>>>
```

La raison pour laquelle vous pouvez accéder à l'attribut `foo` sur les instances est que Python vérifie toujours le dictionnaire de la classe s'il ne trouve pas quelque chose sur l'instance elle-même.

Note : Cette partie de l'exercice illustre ce qu'on appelle une variable de classe. Par exemple, imaginez que vous avez une classe comme ceci :

```python
class Foo(object):
     a = 13                  # Variable de classe
     def __init__(self,b):
         self.b = b          # Variable d'instance
```

Dans cette classe, la variable `a`, assignée dans le corps de la classe elle-même, est une "variable de classe". Elle est partagée par toutes les instances qui sont créées. Par exemple :

```python
>>> f = Foo(10)
>>> g = Foo(20)
>>> f.a          # Vérifiez la variable de classe (identique pour les deux instances)
13
>>> g.a
13
>>> f.b          # Vérifiez la variable d'instance (différente)
10
>>> g.b
20
>>> Foo.a = 42   # Changez la valeur de la variable de classe
>>> f.a
42
>>> g.a
42
>>>
```
