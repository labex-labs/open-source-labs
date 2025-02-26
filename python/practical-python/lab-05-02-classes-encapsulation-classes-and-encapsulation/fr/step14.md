# Exercice 5.8 : Ajout de slots

Modifiez la classe `Stock` de sorte qu'elle ait un attribut `__slots__`. Ensuite, vérifiez qu'il n'est pas possible d'ajouter de nouveaux attributs :

```python
>>> ================================ RESTART ================================
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.10)
>>> s.name
'GOOG'
>>> s.blah = 42
... voir ce qui se passe...
>>>
```

Lorsque vous utilisez `__slots__`, Python utilise une représentation interne plus efficace des objets. Que se passe-t-il si vous essayez d'inspecter le dictionnaire sous-jacent de `s` ci-dessus?

```python
>>> s.__dict__
... voir ce qui se passe...
>>>
```

Il est important de noter que `__slots__` est le plus souvent utilisé comme une optimisation pour les classes servant de structures de données. L'utilisation de slots fera en sorte que de tels programmes utilisent beaucoup moins de mémoire et fonctionnent un peu plus rapidement. Cependant, vous devriez probablement éviter d'utiliser `__slots__` pour la plupart des autres classes.
