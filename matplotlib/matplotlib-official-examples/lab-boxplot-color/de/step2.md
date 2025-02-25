# Erstellen von zufälligen Testdaten

Als nächstes werden wir zufällige Testdaten mit der `numpy`-Bibliothek erstellen. Wir werden 3 Datensätze generieren, von denen jeder eine unterschiedliche Standardabweichung hat.

```python
np.random.seed(19680801)
all_data = [np.random.normal(0, std, size=100) for std in range(1, 4)]
labels = ['x1', 'x2', 'x3']
```
