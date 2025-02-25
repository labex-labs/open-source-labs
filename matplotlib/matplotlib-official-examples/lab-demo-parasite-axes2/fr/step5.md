# Définir les limites et les étiquettes des axes

Nous allons définir les limites et les étiquettes des axes x et y pour chaque axe à l'aide de la fonction `set()`.

```python
host.set(xlim=(0, 2), ylim=(0, 2), xlabel="Distance", ylabel="Density")
par1.set(ylim=(0, 4), ylabel="Temperature")
par2.set(ylim=(1, 65), ylabel="Velocity")
```
