# Vorbereiten der Daten

Wir nehmen nur die ersten beiden Merkmale des Iris-Datensatzes, nämlich die Kelchblätchenlänge und die Kelchblätchenbreite. Anschließend teilen wir die Daten in die Merkmalsmatrix `X` und den Zielvektor `y` auf.

```python
X = iris.data[:, :2]
y = iris.target
```
