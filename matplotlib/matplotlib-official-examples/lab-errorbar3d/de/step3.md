# Daten für das Diagramm generieren

Wir generieren die Daten für unser Diagramm, indem wir eine parametrische Kurve erstellen. Eine parametrische Kurve ist eine Menge von Gleichungen, die die x-, y- und z-Koordinaten als Funktion eines Parameters beschreiben. Wir verwenden die `arange`-Funktion von NumPy, um ein Array von Werten von 0 bis 2π zu erstellen. Anschließend verwenden wir diese Werte, um die x-, y- und z-Koordinaten mit trigonometrischen Funktionen zu berechnen.

```python
t = np.arange(0, 2*np.pi+.1, 0.01)
x, y, z = np.sin(t), np.cos(3*t), np.sin(5*t)
```
