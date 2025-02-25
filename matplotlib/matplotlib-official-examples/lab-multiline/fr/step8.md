# Personnaliser les étiquettes de l'axe des x

Pour personnaliser les étiquettes de l'axe des x, nous pouvons utiliser la fonction `set_xticks`. Nous pouvons spécifier les positions et les étiquettes des repères.

```python
ax1.set_xticks([0.2, 0.4, 0.6, 0.8, 1.],
               labels=["Jan\n2009", "Feb\n2009", "Mar\n2009", "Apr\n2009",
                       "May\n2009"])
```
