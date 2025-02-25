# Setzen auf NaN

Wir werden die Werte, bei denen y > 0,7, auf NaN setzen. Wir werden ein neues y-Array mit NaN-Werten erstellen.

```python
y4 = y.copy()
y4[y3 > 0.7] = np.nan
```
