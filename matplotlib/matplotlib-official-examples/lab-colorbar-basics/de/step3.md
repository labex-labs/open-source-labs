# Erstellen eines Plots und einer Farbskala für positive Daten

Wir erstellen einen Plot der positiven Daten und fügen mithilfe der `colorbar`-Funktion eine Farbskala zum Plot hinzu.

```python
# plot just the positive data and save the
# color "mappable" object returned by ax1.imshow
pos = plt.imshow(Zpos, cmap='Blues', interpolation='none')

# add the colorbar using the figure's method,
# telling which mappable we're talking about and
# which axes object it should be near
plt.colorbar(pos)
```
