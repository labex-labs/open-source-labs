# Hillshading anpassen

In diesem Schritt passen wir das Hillshading an, indem wir das integrierte Shading überschreiben und die RGB-Farben der geschatteten Fläche, die aus "shade" berechnet wurden, übergeben.

```python
# Plot einrichten
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))

ls = LightSource(270, 45)
# Um einen benutzerdefinierten Hillshading-Modus zu verwenden, überschreiben Sie das integrierte Shading und übergeben
# die rgb-Farben der geschatteten Fläche, berechnet aus "shade".
rgb = ls.shade(z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=rgb,
                       linewidth=0, antialiased=False, shade=False)

plt.show()
```
