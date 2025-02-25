# Erstellen des Plots

Jetzt, da wir unsere normalisierten Daten haben, können wir den Plot erstellen. Wir werden die `imshow`-Funktion verwenden, um die Daten als Bild anzuzeigen, und wir werden auch einigen Text zum Plot hinzufügen, um anzuzeigen, was wir betrachten.

```python
dpi = 72
width = 10
height = 10*yn/xn
fig = plt.figure(figsize=(width, height), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1], frameon=False, aspect=1)

light = colors.LightSource(azdeg=315, altdeg=10)
M = light.shade(M, cmap=plt.cm.hot, vert_exag=1.5,
                norm=colors.PowerNorm(0.3), blend_mode='hsv')
ax.imshow(M, extent=[xmin, xmax, ymin, ymax], interpolation="bicubic")
ax.set_xticks([])
ax.set_yticks([])

year = time.strftime("%Y")
text = ("The Mandelbrot fractal set\n"
        "Rendered with matplotlib %s, %s - https://matplotlib.org"
        % (matplotlib.__version__, year))
ax.text(xmin+.025, ymin+.025, text, color="white", fontsize=12, alpha=0.5)

plt.show()
```
