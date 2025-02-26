# Les closures comme une structure de données

Une utilisation potentielle des closures est comme un outil pour l'encapsulation de données. Essayez cet exemple :

```python
def counter(value):
    def incr():
        nonlocal value
        value += 1
        return value

    def decr():
        nonlocal value
        value -= 1
        return value

    return incr, decr
```

Ce code définit deux fonctions internes qui manipulent une valeur. Essayez-le :

```python
>>> up, down = counter(0)
>>> up()
1
>>> up()
2
>>> up()
3
>>> down()
2
>>> down()
1
>>>
```

Remarquez qu'aucune définition de classe n'est impliquée ici. De plus, il n'y a pas non plus de variable globale. Pourtant, les fonctions `up()` et `down()` manipulent une certaine valeur "en coulisse". C'est assez magique.
