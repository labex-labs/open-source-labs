# Datensatz erstellen

Wir werden einen Datensatz mit 3 Merkmalen erstellen, wobei das erste Merkmal eine lineare Beziehung zum Ziel hat, das zweite Merkmal eine nicht-lineare Beziehung zum Ziel hat und das dritte Merkmal völlig irrelevant ist. Für diesen Datensatz werden wir 1000 Stichproben erstellen.

```python
np.random.seed(0)
X = np.random.rand(1000, 3)
y = X[:, 0] + np.sin(6 * np.pi * X[:, 1]) + 0.1 * np.random.randn(1000)
```
