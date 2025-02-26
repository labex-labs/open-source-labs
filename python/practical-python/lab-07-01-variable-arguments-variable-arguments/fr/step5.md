# Exercice 7.1 : Un exemple simple d'arguments variables

Essayez de définir la fonction suivante :

```python
>>> def avg(x,*more):
        return float(x+sum(more))/(1+len(more))

>>> avg(10,11)
10.5
>>> avg(3,4,5)
4.0
>>> avg(1,2,3,4,5,6)
3.5
>>>
```

Remarquez comment le paramètre `*more` collecte tous les arguments supplémentaires.
