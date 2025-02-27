# Daten erstellen

Wir werden einen Datensatz von 20 Punkten erstellen, wobei die ersten 10 Punkte zur Klasse 1 gehören und die letzten 10 Punkte zur Klasse -1 gehören.

```python
np.random.seed(0)
X = np.r_[np.random.randn(10, 2) + [1, 1], np.random.randn(10, 2)]
y = [1] * 10 + [-1] * 10
```
