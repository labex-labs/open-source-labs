# Daten erstellen

Als nächstes werden wir die Daten erstellen, die zum Erstellen des Windbubenplots verwendet werden. Wir werden ein gleichmäßiges Gitter von 5x5 und ein Vektorfeld mithilfe der `meshgrid`- und Multiplikationsfunktionen erstellen.

```python
x = np.linspace(-5, 5, 5)
X, Y = np.meshgrid(x, x)
U, V = 12 * X, 12 * Y
```
