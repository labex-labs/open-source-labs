# Erstellen eines Plots und einer Farbskala für negative Daten

Wir erstellen einen Plot der negativen Daten und fügen mithilfe der `colorbar`-Funktion eine Farbskala zum Plot hinzu. Diesmal legen wir die Position der Farbskala sowie die Parameter `anchor` und `shrink` fest.

```python
# repeat everything above for the negative data
# you can specify location, anchor and shrink the colorbar
neg = plt.imshow(Zneg, cmap='Reds_r', interpolation='none')
plt.colorbar(neg, location='right', anchor=(0, 0.3), shrink=0.7)
```
