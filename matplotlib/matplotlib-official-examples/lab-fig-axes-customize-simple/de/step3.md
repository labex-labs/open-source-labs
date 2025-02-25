# Hinzufügen von Achsen zur Figur

Wir werden Achsen zur Figur mit der `fig.add_axes()`-Methode hinzufügen. Wir werden auch die Hintergrundfarbe der Achsen mit der `rect.set_facecolor()`-Methode festlegen.

```python
ax1 = fig.add_axes([0.1, 0.3, 0.4, 0.4])
rect = ax1.patch
rect.set_facecolor('lightslategray')
```
