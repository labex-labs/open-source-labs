# Daten generieren

Wir werden Daten mit NumPy generieren. Wir werden 100 Datenpunkte mit einer gleichmäßigen Verteilung zwischen 0 und 5 generieren. Wir werden den Schwellenwert auf 2,5 setzen und die Labels mit einem booleschen Ausdruck generieren. Wir werden die ersten 50 Datenpunkte als Trainingsdaten und die verbleibenden als Testdaten verwenden.

```python
train_size = 50
rng = np.random.RandomState(0)
X = rng.uniform(0, 5, 100)[:, np.newaxis]
y = np.array(X[:, 0] > 2.5, dtype=int)
```
