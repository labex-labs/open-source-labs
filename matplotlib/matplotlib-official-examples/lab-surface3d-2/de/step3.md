# Erstellen des 3D-Oberflächenplots

Jetzt können wir den 3D-Oberflächenplot erstellen. Wir beginnen damit, eine Figur zu erstellen und ein Subplot hinzuzufügen, indem wir das Argument `projection='3d'` verwenden. Anschließend verwenden wir die `plot_surface()`-Funktion, um die Oberfläche mit den Daten zu zeichnen, die wir im vorherigen Schritt erstellt haben.

```python
# Plot the surface
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z)
```
