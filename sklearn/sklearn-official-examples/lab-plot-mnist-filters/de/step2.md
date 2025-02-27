# Daten laden

Als nächstes laden wir den MNIST-Datensatz mit der Funktion `fetch_openml` von Scikit-learn.

```python
X, y = fetch_openml(
    "mnist_784", version=1, return_X_y=True, as_frame=False, parser="pandas"
)
```
