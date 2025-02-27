# Daten erstellen

Wir werden drei verschiedene Datensätze erstellen, um die Verwendung von t-SNE zu veranschaulichen. Der erste Datensatz wird aus zwei konzentrischen Kreisen bestehen.

```python
n_samples = 150
n_components = 2

X, y = datasets.make_circles(
    n_samples=n_samples, factor=0.5, noise=0.05, random_state=0
)

red = y == 0
green = y == 1
```
