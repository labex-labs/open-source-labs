# Kreis und Startpunkt zeichnen

Der dritte Schritt besteht darin, den Kreis und den Startpunkt auf dem linken Teilplot zu zeichnen. Wir erstellen ein Array von Winkeln, um den Kreis zu generieren, und plotten dann die Sinus- und Kosinuswerte jedes Winkels. Wir plotten auch einen einzelnen Punkt am Ursprung.

```python
x = np.linspace(0, 2 * np.pi, 50)
axl.plot(np.cos(x), np.sin(x), "k", lw=0.3)
point, = axl.plot(0, 0, "o")
```
