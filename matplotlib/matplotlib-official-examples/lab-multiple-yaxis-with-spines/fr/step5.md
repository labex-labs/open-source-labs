# Ajoutez des données au tracé

Nous ajoutons des données au tracé en utilisant la méthode `plot`. Nous ajoutons trois lignes au tracé, chacune avec un axe y différent.

```python
p1, = ax.plot([0, 1, 2], [0, 1, 2], "C0", label="Density")
p2, = twin1.plot([0, 1, 2], [0, 3, 2], "C1", label="Temperature")
p3, = twin2.plot([0, 1, 2], [50, 30, 15], "C2", label="Velocity")
```
