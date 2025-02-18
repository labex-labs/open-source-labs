# Positionnement vertical manuel

Spécifiez manuellement la position verticale du titre en utilisant le paramètre `y` de la fonction `title()`.

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.xaxis.set_label_position('top')
ax.set_xlabel('X-label')
ax.set_title('Manual Y Positioning', y=1.0)
```
