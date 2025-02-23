# Form-Annotation hinzufügen

Formen können verwendet werden, um auf bestimmte Bereiche eines Graphen aufmerksam zu machen. In diesem Schritt werden wir ein Rechteck hinzufügen, um den Bereich zwischen x = 1 und x = 3 hervorzuheben.

```python
# Add shape annotation
ax.axvspan(1, 3, facecolor='gray', alpha=0.2)
plt.show()
```
