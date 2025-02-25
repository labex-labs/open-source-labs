# Das Diagramm zeichnen

Jetzt, wo wir unsere Beispiel-Daten haben, können wir das Diagramm mit der `errorbar()`-Funktion zeichnen. Wir werden die `x`- und `y`-Arrays als die ersten beiden Parameter übergeben. Anschließend werden wir die Fehler in x-Richtung als 0,2 und die Fehler in y-Richtung als 0,4 mithilfe der Parameter `xerr` und `yerr` angeben.

```python
fig, ax = plt.subplots()
ax.errorbar(x, y, xerr=0.2, yerr=0.4)
plt.show()
```
