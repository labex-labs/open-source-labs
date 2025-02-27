# Daten laden und mischen

Wir laden zunächst die Ziffern-Datenmenge und mischen die Daten zufällig.

```python
digits = datasets.load_digits()
rng = np.random.RandomState(2)
indices = np.arange(len(digits.data))
rng.shuffle(indices)
```