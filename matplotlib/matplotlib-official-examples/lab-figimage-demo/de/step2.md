# Erstellen der Figur und des Bilds

Als nächstes erstellen wir die Figur und das Bild, das wir in sie platzieren möchten. In diesem Beispiel erstellen wir ein 100x100 Array von Zufallswerten und setzen die Werte in der rechten Hälfte des Bilds auf 1. Anschließend erstellen wir zwei separate Instanzen des Bilds, jede mit einer anderen Position und Opazität.

```python
fig = plt.figure()
Z = np.arange(10000).reshape((100, 100))
Z[:, 50:] = 1

im1 = fig.figimage(Z, xo=50, yo=0, origin='lower')
im2 = fig.figimage(Z, xo=100, yo=100, alpha=.8, origin='lower')
```
