# Entfernen von Punkten

Wir werden die Punkte entfernen, bei denen y > 0,7. Wir werden ein neues x-Array und y-Array erstellen, die nur die verbleibenden Punkte enthalten.

```python
x2 = x[y <= 0.7]
y2 = y[y <= 0.7]
```
