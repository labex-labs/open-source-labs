# Ajouter une annotation avec une flèche

Les flèches peuvent être utilisées pour pointer des caractéristiques ou des tendances spécifiques dans un graphique. Dans cette étape, nous allons ajouter une flèche au graphique qui pointe vers la valeur maximale.

```python
# Find the maximum value
y = [0, 1, 4, 9, 16]
max_index = y.index(max(y))
xmax = max_index
ymax = y[max_index]

# Add arrow annotation
ax.annotate('Maximum Value', xy=(xmax, ymax), xytext=(xmax, ymax + 5),
            arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()
```
