# Clamp Number

Écrivez une fonction `clamp_number(num, a, b)` qui prend trois paramètres :

- `num` (entier ou flottant) : le nombre à restreindre
- `a` (entier ou flottant) : la borne inférieure de la plage
- `b` (entier ou flottant) : la borne supérieure de la plage

La fonction doit restreindre `num` dans la plage inclusive spécifiée par les valeurs limites. Si `num` est dans la plage (`a`, `b`), renvoyez `num`. Sinon, renvoyez le nombre le plus proche dans la plage.

```python
def clamp_number(num, a, b):
  return max(min(num, max(a, b)), min(a, b))
```

```python
clamp_number(2, 3, 5) # 3
clamp_number(1, -1, -5) # -1
```
