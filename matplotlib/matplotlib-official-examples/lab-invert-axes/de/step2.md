# Daten erstellen

Als nächstes müssen wir einige Daten zum Plotten erstellen. In diesem Beispiel werden wir ein Array von Zeitwerten (`t`) und ein Array von Spannungswerten (`s`) erstellen.

```python
t = np.arange(0.01, 5.0, 0.01)
s = np.exp(-t)
```
