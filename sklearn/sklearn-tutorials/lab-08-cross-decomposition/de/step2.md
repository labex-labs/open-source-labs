# Laden des Datensatzes

Als nächstes laden wir einen Beispiel-Datensatz, um die Cross-Decomposition-Algorithmen zu demonstrieren. Aus Gründen der Einfachheit erstellen wir zwei Matrizen `X` und `Y` mit zufälligen Werten.

```python
np.random.seed(0)
X = np.random.random((100, 5))
Y = np.random.random((100, 3))
```
