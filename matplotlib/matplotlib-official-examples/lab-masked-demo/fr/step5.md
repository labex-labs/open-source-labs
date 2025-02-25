# Affectez NaN

Nous allons affecter NaN là où y > 0,7. Nous allons créer un nouveau tableau y avec des valeurs NaN.

```python
y4 = y.copy()
y4[y3 > 0.7] = np.nan
```
