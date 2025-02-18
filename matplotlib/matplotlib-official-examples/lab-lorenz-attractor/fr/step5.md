# Tracer l'attracteur de Lorenz

Nous traçons l'attracteur de Lorenz en utilisant le module mplot3d de Matplotlib.

```python
ax = plt.figure().add_subplot(projection='3d')

ax.plot(*xyzs.T, lw=0.5)
ax.set_xlabel("Axe des X")
ax.set_ylabel("Axe des Y")
ax.set_zlabel("Axe des Z")
ax.set_title("Attracteur de Lorenz")

plt.show()
```
