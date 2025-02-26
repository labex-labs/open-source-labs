# Exercice 6.14 : Expressions de générateur dans les arguments de fonction

Les expressions de générateur sont parfois utilisées dans les arguments de fonction. Cela peut paraître un peu étrange au premier abord, mais essayez cet exemple :

```python
>>> nums = [1,2,3,4,5]
>>> sum([x*x for x in nums])    # Une compréhension de liste
55
>>> sum(x*x for x in nums)      # Une expression de générateur
55
>>>
```

Dans l'exemple ci-dessus, la deuxième version utilisant des générateurs utiliserait beaucoup moins de mémoire si une grande liste était manipulée.

Dans votre fichier `portfolio.py`, vous avez effectué quelques calculs impliquant des compréhensions de liste. Essayez de les remplacer par des expressions de générateur.
