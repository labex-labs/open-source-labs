# Erstellen einer Grafik

Als nächstes werden wir eine Grafik mit der `imshow`-Funktion von Matplotlib erstellen. Diese Funktion zeigt ein Bild auf der Grafik an. Wir werden auch eine Figur mit zwei Teilgrafiken erstellen.

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.subplots_adjust(wspace=0.5)

im1 = ax1.imshow([[1, 2], [3, 4]])

im2 = ax2.imshow([[1, 2], [3, 4]])
```
