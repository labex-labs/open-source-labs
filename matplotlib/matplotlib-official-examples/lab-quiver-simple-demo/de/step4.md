# Den Pfeilschlüssel erstellen

Wir können einen Pfeilschlüssel zum Plot hinzufügen, um die Skala der Pfeile anzuzeigen. Wir verwenden die Funktion `ax.quiverkey()`, um den Schlüssel hinzuzufügen. Wir übergeben das `q`-Objekt, die `X`- und `Y`-Position des Schlüssels, die Länge des Pfeils, das Label für den Schlüssel und die Position des Labels.

```python
ax.quiverkey(q, X=0.3, Y=1.1, U=10,
             label='Quiver key, length = 10', labelpos='E')
```
