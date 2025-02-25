# Map Number to Range

Écrivez une fonction appelée `num_to_range` qui prend cinq arguments : `num`, `inMin`, `inMax`, `outMin` et `outMax`. La fonction devrait renvoyer `num` mis en correspondance entre `outMin`-`outMax` à partir de `inMin`-`inMax`. En d'autres termes, la fonction devrait prendre un nombre (`num`) qui se situe dans une certaine plage (`inMin`-`inMax`) et le mapper dans une nouvelle plage (`outMin`-`outMax`).

```python
def num_to_range(num, inMin, inMax, outMin, outMax):
  return outMin + (float(num - inMin) / float(inMax - inMin) * (outMax
                  - outMin))
```

```python
num_to_range(5, 0, 10, 0, 100) # 50.0
```
