# Die Fläche darstellen

```python
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
```

Wir stellen die Fläche mit der Funktion `plot_surface()` dar. Wir übergeben die `X`-, `Y`- und `Z`-Werte sowie den Parameter `cmap`, der auf `cm.coolwarm` gesetzt ist, um die Fläche mit der Farbpalette coolwarm zu färben. Wir setzen auch `linewidth=0`, um das Gitter zu entfernen, und `antialiased=False`, um die Fläche als undurchsichtig darzustellen.
