# Koordinaten transformieren

Der nächste Schritt besteht darin, die Koordinaten der Daten und der Anzeige zu transformieren. Wir werden die Methode `ax.transData` verwenden, um die Datenkoordinaten zu transformieren, und das Koordinatensystem `figure pixels`, um die Anzeige-Koordinaten zu transformieren.

```python
xdata, ydata = 5, 0
xdisplay, ydisplay = ax.transData.transform((xdata, ydata))
```
