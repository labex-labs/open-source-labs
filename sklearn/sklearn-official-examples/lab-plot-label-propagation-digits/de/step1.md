# Daten laden und mischen

Zunächst laden wir den Datensatz mit den handschriftlichen Ziffern (digits dataset) und mischen die Daten zufällig.

```python
digits = datasets.load_digits()
rng = np.random.RandomState(2)
indices = np.arange(len(digits.data))
rng.shuffle(indices)
```
