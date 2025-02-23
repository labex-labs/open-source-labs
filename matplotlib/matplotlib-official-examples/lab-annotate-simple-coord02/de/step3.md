# Pfeil-Annotation hinzufügen

Pfeile können verwendet werden, um bestimmte Merkmale oder Trends in einem Graphen anzuzeigen. In diesem Schritt werden wir einen Pfeil zum Graphen hinzufügen, der auf den Maximalwert zeigt.

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
