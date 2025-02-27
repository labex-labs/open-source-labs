# Gegenseitige Information berechnen

Wir werden nun den Wert der gegenseitigen Information für jedes Merkmal berechnen. Die gegenseitige Information kann jede Art von Abhängigkeit zwischen Variablen erfassen. Wir werden die Werte der gegenseitigen Information normalisieren, indem wir sie durch den maximalen Wert der gegenseitigen Information dividieren.

```python
mi = mutual_info_regression(X, y)
mi /= np.max(mi)
```
