# Erstellen einer Figur und eines ImageGrid-Objekts

Als nächstes erstellen wir ein `figure`-Objekt mit der `plt.figure`-Funktion und übergeben das `figsize`-Argument, um die Größe der Figur festzulegen. Anschließend erstellen wir ein `ImageGrid`-Objekt mit der `ImageGrid`-Funktion und übergeben das `figure`, `111` als Subplot-Argument, `(2, 2)` als `nrows_ncols`-Argument, um ein 2x2-Gitter von Achsen zu erstellen, und `0.1` als `axes_pad`-Argument, um den Abstand zwischen den Achsen festzulegen.

```python
fig = plt.figure(figsize=(4., 4.))
grid = ImageGrid(fig, 111, nrows_ncols=(2, 2), axes_pad=0.1)
```
