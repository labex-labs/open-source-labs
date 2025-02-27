# Erstellen des XOR-Datensatzes

In diesem Schritt werden wir einen XOR-Datensatz mit numpy erstellen. Wir werden die Funktion `logical_xor` verwenden, um die Labels basierend auf den Eingabefeatures zu erstellen.

```python
xx, yy = np.meshgrid(np.linspace(-3, 3, 50), np.linspace(-3, 3, 50))
rng = np.random.RandomState(0)
X = rng.randn(200, 2)
Y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0)
```
