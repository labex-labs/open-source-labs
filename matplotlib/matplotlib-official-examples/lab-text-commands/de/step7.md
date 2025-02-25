# Hinzufügen von Anmerkungen zum Plot

Wir können Anmerkungen zum Plot hinzufügen, indem wir die Funktion `ax.annotate()` verwenden. Diese Funktion nimmt drei Argumente entgegen: den Anmerkungstext, die xy-Koordinate des Punktes, den wir annotieren möchten, und die xy-Koordinate der Textposition. Wir können den Anmerkungsstil mit dem Argument `arrowprops` anpassen.

```python
ax.annotate('annotate', xy=(2, 1), xytext=(3, 4),
            arrowprops=dict(facecolor='black', shrink=0.05))
```
