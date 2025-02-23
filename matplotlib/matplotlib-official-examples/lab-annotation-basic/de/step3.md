# Das Diagramm annotieren

Jetzt werden wir das Diagramm annotieren, indem wir einen Pfeil hinzufügen, der auf eine bestimmte Koordinate zeigt. In diesem Beispiel werden wir einen Pfeil hinzufügen, der auf das lokale Maximum der Kosinusfunktion zeigt.

```python
ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
```

Die `ax.annotate()`-Funktion nimmt mehrere Argumente entgegen. Das erste Argument ist der Text, der auf dem Diagramm angezeigt werden soll. Das `xy`-Argument gibt die Koordinaten des Punktes an, den wir annotieren möchten. Das `xytext`-Argument gibt die Koordinaten des Texts an. Das `arrowprops`-Argument ist ein Wörterbuch, das die Eigenschaften des Pfeils angibt.
