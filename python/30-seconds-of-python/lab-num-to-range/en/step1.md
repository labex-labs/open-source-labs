# Map Number to Range

Write a function called `num_to_range` that takes five arguments: `num`, `inMin`, `inMax`, `outMin`, and `outMax`. The function should return `num` mapped between `outMin`-`outMax` from `inMin`-`inMax`. In other words, the function should take a number (`num`) that falls within a certain range (`inMin`-`inMax`) and map it to a new range (`outMin`-`outMax`).

```python
def num_to_range(num, inMin, inMax, outMin, outMax):
  return outMin + (float(num - inMin) / float(inMax - inMin) * (outMax
                  - outMin))
```

```python
num_to_range(5, 0, 10, 0, 100) # 50.0
```
