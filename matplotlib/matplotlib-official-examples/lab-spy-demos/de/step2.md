# Erstellen eines zufälligen Arrays

Als nächstes werden wir ein zufälliges Array mit den Dimensionen (20, 20) mithilfe der `numpy.random.randn`-Funktion erstellen. Wir werden auch einige Elemente auf Null setzen, um eine spärliche Matrix zu erstellen.

```python
np.random.seed(19680801)
x = np.random.randn(20, 20)
x[5, :] = 0.
x[:, 12] = 0.
```
