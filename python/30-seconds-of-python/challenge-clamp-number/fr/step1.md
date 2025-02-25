# Défi du nombre clamps

## Problème

Écrivez une fonction `clamp_number(num, a, b)` qui prend trois paramètres :

- `num` (entier ou flottant) : le nombre à clamer
- `a` (entier ou flottant) : la borne inférieure de la plage
- `b` (entier ou flottant) : la borne supérieure de la plage

La fonction doit clamer `num` dans la plage inclusive spécifiée par les valeurs limites. Si `num` est dans la plage (`a`, `b`), renvoyez `num`. Sinon, renvoyez le nombre le plus proche dans la plage.

## Exemple

```python
clamp_number(2, 3, 5) # 3
clamp_number(1, -1, -5) # -1
clamp_number(10, 1, 5) # 5
clamp_number(-10, -5, -1) # -5
```
