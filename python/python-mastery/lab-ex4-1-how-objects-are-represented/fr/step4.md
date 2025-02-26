# Le rôle des classes

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
>>> SimpleStock.__dict__['cost']
... regardez la sortie...
>>>
```

Essayez d'appeler directement la méthode `cost()` à travers le dictionnaire :

```python
>>> SimpleStock.__dict__['cost'](goog)
49010.00
>>> SimpleStock.__dict__['cost'](ibm)
4561.5
>>>
```

Remarquez comment vous appelez la fonction définie dans la définition de classe et comment l'argument `self` obtient l'instance.

Si vous ajoutez une nouvelle valeur à la classe, elle devient une variable de classe visible par toutes les instances. Essayez :

```python
>>> SimpleStock.spam = 42
>>> ibm.spam
42
>>> goog.spam
42
>>>
```

Observez que `spam` n'est pas partie du dictionnaire d'instance.

```python
>>> ibm.__dict__
... regardez la sortie...
>>>
```

Au lieu de cela, il est partie du dictionnaire de classe :

```python
>>> SimpleStock.__dict__['spam']
42
>>>
```

Essentiellement, voilà tout ce qu'est réellement une classe - c'est une collection de valeurs partagées par les instances.
