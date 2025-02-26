# Übung 7.1: Ein einfaches Beispiel mit variablen Argumenten

Versuchen Sie, die folgende Funktion zu definieren:

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

Bemerken Sie, wie der Parameter `*more` alle zusätzlichen Argumente sammelt.
