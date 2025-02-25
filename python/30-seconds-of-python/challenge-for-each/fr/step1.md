# Exécuter une fonction pour chaque élément de la liste

## Problème

Écrivez une fonction `for_each(itr, fn)` qui prend une liste `itr` et une fonction `fn` en arguments. La fonction devrait exécuter `fn` une fois pour chaque élément de `itr`.

## Exemple

```python
def print_square(num):
    print(num*num)

for_each([1, 2, 3], print_square) # affiche 1 4 9
```

Dans l'exemple ci-dessus, la fonction `for_each` est appelée avec une liste `[1, 2, 3]` et une fonction `print_square`. La fonction `print_square` est exécutée une fois pour chaque élément de la liste, affichant le carré de chaque nombre.
