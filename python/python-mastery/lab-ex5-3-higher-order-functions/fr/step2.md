# Mappage

L'une des opérations les plus courantes en programmation fonctionnelle est l'opération `map()` qui applique une fonction aux valeurs d'une séquence. Python a une fonction intégrée `map()` qui effectue cette opération. Par exemple :

```python
>>> nums = [1,2,3,4]
>>> squares = map(lambda x: x*x, nums)
>>> for n in squares:
        print(n)

1
4
9
16
>>>
```

`map()` produit un itérateur, donc si vous voulez une liste, vous devrez la créer explicitement :

```python
>>> squares = list(map(lambda x: x*x, nums))
>>> squares
[1, 4, 9, 16]
>>>
```

Essayez d'utiliser `map()` dans votre fonction `convert_csv()`.
