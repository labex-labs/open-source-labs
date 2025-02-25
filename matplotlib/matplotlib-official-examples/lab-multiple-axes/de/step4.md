# Sinuskurve zeichnen

Der vierte Schritt besteht darin, die Sinuskurve auf dem rechten Teilplot zu zeichnen. Wir erstellen ein Array von Winkeln und plotten dann den Sinuswert jedes Winkels. Wir speichern auch das `sine`-Plot-Objekt, das wir später in der Animation aktualisieren werden.

```python
sine, = axr.plot(x, np.sin(x))
```
