# Tracer les données

Nous allons tracer trois jeux de données sur le même graphique : la densité, la température et la vitesse. Nous utiliserons la fonction `plot()` pour tracer les données.

```python
p1, = host.plot([0, 1, 2], [0, 1, 2], label="Density")
p2, = par1.plot([0, 1, 2], [0, 3, 2], label="Temperature")
p3, = par2.plot([0, 1, 2], [50, 30, 15], label="Velocity")
```
