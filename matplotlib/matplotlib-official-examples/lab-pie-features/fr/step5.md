# Personnaliser les couleurs

Nous pouvons personnaliser les couleurs des tranches en passant une liste de couleurs au paramètre `colors` de la fonction `pie()`.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=['olivedrab', 'rosybrown', 'gray','saddlebrown'])
```
