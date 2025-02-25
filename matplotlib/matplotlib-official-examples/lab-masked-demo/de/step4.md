# Maskieren von Punkten

Wir werden Punkte maskieren, bei denen y > 0,7, indem wir ein maskiertes Array verwenden. Wir werden ein neues y-Array mit maskierten Werten erstellen.

```python
y3 = np.ma.masked_where(y > 0.7, y)
```
