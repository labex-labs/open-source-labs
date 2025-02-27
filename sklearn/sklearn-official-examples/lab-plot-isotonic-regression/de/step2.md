# Daten generieren

Als nächstes werden wir einige Daten generieren, die wir für unsere Regression verwenden. Wir werden einen nicht-linearen monotonen Trend mit homoskedastischem gleichförmigem Rauschen erstellen.

```python
n = 100
x = np.arange(n)
rs = check_random_state(0)
y = rs.randint(-50, 50, size=(n,)) + 50.0 * np.log1p(np.arange(n))
```
