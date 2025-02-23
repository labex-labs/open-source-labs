# Tracer des données 2D sur le tracé 3D

La troisième étape consiste à tracer des données 2D sur le tracé 3D à l'aide de `ax.plot` et `ax.scatter`. La fonction `ax.plot` trace une courbe sinusoidale en utilisant les axes x et y. La fonction `ax.scatter` trace des données de nuage de points sur les axes x et z.

```python
# Trace une courbe sinusoidale en utilisant les axes x et y.
x = np.linspace(0, 1, 100)
y = np.sin(x * 2 * np.pi) / 2 + 0.5
ax.plot(x, y, zs=0, zdir='z', label='courbe dans (x, y)')

# Trace des données de nuage de points (20 points 2D par couleur) sur les axes x et z.
colors = ('r', 'g', 'b', 'k')

# Fixation de l'état aléatoire pour la reproductibilité
np.random.seed(19680801)

x = np.random.sample(20 * len(colors))
y = np.random.sample(20 * len(colors))
c_list = []
for c in colors:
    c_list.extend([c] * 20)
# En utilisant zdir='y', la valeur y de ces points est fixée à la valeur zs 0
# et les points (x, y) sont tracés sur les axes x et z.
ax.scatter(x, y, zs=0, zdir='y', c=c_list, label='points dans (x, z)')
```
