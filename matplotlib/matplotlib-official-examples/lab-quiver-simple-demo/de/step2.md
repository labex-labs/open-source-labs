# Daten erstellen

Wir müssen die `X`- und `Y`-Koordinaten mit der Funktion `np.meshgrid()` erstellen. Anschließend erstellen wir die Arrays `U` und `V`, die die Vektorfelder repräsentieren.

```python
X = np.arange(-10, 10, 1)
Y = np.arange(-10, 10, 1)
U, V = np.meshgrid(X, Y)
```
