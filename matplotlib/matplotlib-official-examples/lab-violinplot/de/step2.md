# Erstellen eines Beispiel-Datensatzes

Wir werden einen Beispiel-Datensatz mit der numpy-Bibliothek erstellen. Wir werden sechs Datensätze mit unterschiedlichen Standardabweichungen erstellen.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# fake data
pos = [1, 2, 4, 5, 7, 8]
data = [np.random.normal(0, std, size=100) for std in pos]
```
