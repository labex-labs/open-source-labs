# Konturieren nach Abstand zu den Ecken des Dreiecks

In diesem Schritt werden wir konturieren, basierend auf dem Abstand zu den Ecken des Dreiecks. Wir werden eine Funktion für den Abstand von einzelnen Punkten definieren und gemäß dieser Funktion konturieren.

```python
# Definiere eine schöne Funktion für den Abstand von einzelnen Punkten
def f(x, y, pts):
    z = np.zeros_like(x)
    for p in pts:
        z = z + 1/(np.sqrt((x - p[0])**2 + (y - p[1])**2))
    return 1/z

X, Y = np.meshgrid(np.linspace(-1, 1, 51), np.linspace(-1, 1, 51))
Z = f(X, Y, pts)

CS = plt.contour(X, Y, Z, 20)

tellme('Verwenden Sie die Maus, um die Konturbeschriftungsorte auszuwählen, die mittlere Maustaste, um zu beenden')
CL = plt.clabel(CS, manual=True)
```
