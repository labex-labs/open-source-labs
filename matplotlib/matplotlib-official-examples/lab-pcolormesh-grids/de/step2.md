# Daten für die Visualisierung erstellen

Als nächstes werden wir ein 2D-Gitter erstellen, das wir zur Visualisierung verwenden werden. Wir können ein Gitter mit der `meshgrid`-Funktion in NumPy erstellen. Die `meshgrid`-Funktion erstellt ein Gitter von Punkten aus zwei Vektoren, `x` und `y`, die die Koordinaten der Gitterpunkte repräsentieren. Wir werden ein Gitter von 5x5 Punkten mit dem folgenden Codeblock erstellen:

```python
nrows = 5
ncols = 5
x = np.arange(ncols + 1)
y = np.arange(nrows + 1)
X, Y = np.meshgrid(x, y)
Z = X + Y
```
