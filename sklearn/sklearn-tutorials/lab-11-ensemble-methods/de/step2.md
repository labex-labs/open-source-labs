# Die Daten laden

Als nächstes laden wir den Iris-Datensatz aus scikit-learn mit der Funktion `load_iris`.

```python
data = load_iris()
X, y = data.data, data.target
```