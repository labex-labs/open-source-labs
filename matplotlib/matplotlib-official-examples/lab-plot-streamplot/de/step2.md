# Daten erstellen

Wir werden die Daten für unseren Streamplot mit der Numpy-Bibliothek erstellen. In diesem Beispiel werden wir ein Gitternetz mit 100 Punkten in beiden Richtungen erstellen und die U- und V-Komponenten unseres Vektorfelds berechnen.

```python
w = 3
Y, X = np.mgrid[-w:w:100j, -w:w:100j]
U = -1 - X**2 + Y
V = 1 + X - Y**2
speed = np.sqrt(U**2 + V**2)
```
