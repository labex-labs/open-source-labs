# Hinzufügen einer Farbskalenreferenz

Um eine Referenz für die Farbskala bereitzustellen, können wir eine Farbskala zur Grafik hinzufügen. Dies kann mit der `colorbar`-Funktion aus `matplotlib.pyplot` erreicht werden.

```python
imgplot = plt.imshow(lum_img)
plt.colorbar()
```