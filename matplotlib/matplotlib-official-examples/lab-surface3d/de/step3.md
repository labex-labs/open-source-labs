# Daten erstellen

```python
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
```

Wir erstellen die Daten für den Graphen. Wir erstellen die `X`- und `Y`-Werte als Arrays mit gleichmäßig verteilten Werten von -5 bis 5 in Schritten von 0,25. Anschließend erstellen wir ein Gitternetz von `X`- und `Y`-Werten mit `np.meshgrid()`. Wir verwenden das Gitternetz, um die `R`-Werte zu berechnen, die die Entfernung vom Ursprung darstellen. Anschließend berechnen wir die `Z`-Werte mit der `sin()`-Funktion von `R`.
