# Erstellen der Würfel und der Verbindung

Jetzt werden wir die beiden Würfel und die Verbindung zwischen ihnen erstellen. Dazu definieren wir drei boolesche Arrays, die zu einem einzigen booleschen Array kombiniert werden. Die ersten beiden Arrays definieren die Position der Würfel, während das dritte Array die Position der Verbindung definiert.

```python
cube1 = (x < 3) & (y < 3) & (z < 3)
cube2 = (x >= 5) & (y >= 5) & (z >= 5)
link = abs(x - y) + abs(y - z) + abs(z - x) <= 2

voxelarray = cube1 | cube2 | link
```
