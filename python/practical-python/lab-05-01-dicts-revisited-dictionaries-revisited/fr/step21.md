# Exercice 5.4 : Méthodes liées

Une caractéristique subtile de Python est que l'appel d'une méthode implique en fait deux étapes et quelque chose appelé une méthode liée. Par exemple :

```python
>>> s = goog.sell
>>> s
<bound method Stock.sell of Stock('GOOG', 100, 490.1)>
>>> s(25)
>>> goog.shares
75
>>>
```

Les méthodes liées contiennent en fait tous les éléments nécessaires pour appeler une méthode. Par exemple, elles conservent une trace de la fonction qui implémente la méthode :

```python
>>> s.__func__
<function sell at 0x10049af50>
>>>
```

C'est la même valeur que celle trouvée dans le dictionnaire de `Stock`.

```python
>>> Stock.__dict__['sell']
<function sell at 0x10049af50>
>>>
```

Les méthodes liées enregistrent également l'instance, qui est l'argument `self`.

```python
>>> s.__self__
Stock('GOOG',75,490.1)
>>>
```

Lorsque vous appelez la fonction en utilisant `()`, tous les éléments se rassemblent. Par exemple, appeler `s(25)` fait en réalité ceci :

```python
>>> s.__func__(s.__self__, 25)    # Identique à s(25)
>>> goog.shares
50
>>>
```
