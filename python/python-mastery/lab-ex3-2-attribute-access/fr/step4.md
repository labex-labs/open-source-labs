# Méthodes liées

Il peut sembler surprenant, mais les appels de méthodes sont superposés à la mécanique utilisée pour les attributs simples. Essentiellement, une méthode est un attribut qui s'exécute lorsque vous ajoutez les parenthèses () requises pour l'appeler comme une fonction. Par exemple :

```python
>>> s = Stock('GOOG',100,490.10)
>>> s.cost           # Recherche la méthode
<bound method Stock.cost of <__main__.Stock object at 0x409530>>
>>> s.cost()         # Recherche et appelle la méthode
49010.0

>>> # Même opérations en utilisant getattr()
>>> getattr(s, 'cost')
<bound method Stock.cost of <__main__.Stock object at 0x409530>>
>>> getattr(s, 'cost')()
49010.0
>>>
```

Une méthode liée est attachée à l'objet d'où elle vient. Si cet objet est modifié, la méthode verra les modifications. Vous pouvez voir l'objet original en inspectant l'attribut `__self__` de la méthode.

```python
>>> c = s.cost
>>> c()
49010.0
>>> s.shares = 75
>>> c()
36757.5
>>> c.__self__
<__main__.Stock object at 0x409530>
>>> c.__func__
<function cost at 0x37cc30>
>>> c.__func__(c.__self__)      # Voce qui se passe en arrière-plan lors de l'appel de c()
36757.5
>>>
```

Essayez-le avec la méthode `sell()` juste pour vous assurer que vous comprenez le fonctionnement :

```python
>>> f = s.sell
>>> f.__func__(f.__self__, 25)     # Identique à s.sell(25)
>>> s.shares
50
>>>
```
