# Vérifiez si un nombre est pair

Écrivez une fonction `is_even(num)` qui prend un nombre en argument et renvoie `True` si le nombre est pair et `False` si le nombre est impair. Pour vérifier si un nombre est pair ou impair, vous pouvez utiliser l'opérateur modulo (`%`). Si un nombre est pair, il n'aura pas de reste lorsqu'il est divisé par 2. Si un nombre est impair, il aura un reste de 1 lorsqu'il est divisé par 2.

```python
def is_even(num):
  return num % 2 == 0
```

```python
is_even(3) # False
```
