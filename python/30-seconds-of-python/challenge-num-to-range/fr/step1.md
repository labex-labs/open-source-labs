# Map Number to Range

## Problème

Écrivez une fonction appelée `num_to_range` qui prend cinq arguments : `num`, `inMin`, `inMax`, `outMin` et `outMax`. La fonction devrait renvoyer `num` mappé entre `outMin`-`outMax` à partir de `inMin`-`inMax`. En d'autres termes, la fonction devrait prendre un nombre (`num`) qui se situe dans une certaine plage (`inMin`-`inMax`) et le mapper dans une nouvelle plage (`outMin`-`outMax`).

## Exemple

```python
num_to_range(5, 0, 10, 0, 100) # 50.0
```

Dans cet exemple, nous map le nombre 5 d'une plage de 0 à 10 à une plage de 0 à 100. Le résultat devrait être 50.0.
