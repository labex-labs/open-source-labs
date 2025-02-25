# Achsengrenzen und -beschriftungen festlegen

Wir werden die x- und y-Achsengrenzen und -beschriftungen für jede Achse mit der `set()`-Funktion festlegen.

```python
host.set(xlim=(0, 2), ylim=(0, 2), xlabel="Distance", ylabel="Density")
par1.set(ylim=(0, 4), ylabel="Temperature")
par2.set(ylim=(1, 65), ylabel="Velocity")
```
