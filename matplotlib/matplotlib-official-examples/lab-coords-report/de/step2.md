# Daten erstellen

Als nächstes werden wir einige zufällige Daten erstellen, die wir in unserer Visualisierung verwenden. In diesem Beispiel werden wir zwei Arrays mit zufälligen Daten mit `numpy` erstellen.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

x = np.random.rand(20)
y = 1e7 * np.random.rand(20)
```
