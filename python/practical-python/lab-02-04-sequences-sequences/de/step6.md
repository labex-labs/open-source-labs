# break-Anweisung

Sie können die `break`-Anweisung verwenden, um frühzeitig aus einer Schleife auszubrechen.

```python
for name in namelist:
    if name == 'Jake':
        break
 ...
 ...
statements
```

Wenn die `break`-Anweisung ausgeführt wird, tritt sie aus der Schleife aus und springt zu den nächsten `statements`. Die `break`-Anweisung betrifft nur die innerste Schleife. Wenn diese Schleife innerhalb einer anderen Schleife befindet, wird die äußere Schleife nicht verlassen.
