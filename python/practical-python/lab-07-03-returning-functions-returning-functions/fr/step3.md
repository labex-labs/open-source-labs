# Closures

Lorsqu'une fonction interne est renvoyée en tant que résultat, cette fonction interne est connue sous le nom de _closure_.

```python
def add(x, y):
    # `do_add` est un closure
    def do_add():
        print('Adding', x, y)
        return x + y
    return do_add
```

_Fonctionnalité essentielle : Un closure conserve les valeurs de toutes les variables nécessaires pour que la fonction puisse fonctionner correctement plus tard._ Pensez à un closure comme une fonction plus un environnement supplémentaire qui contient les valeurs des variables dont elle dépend.
