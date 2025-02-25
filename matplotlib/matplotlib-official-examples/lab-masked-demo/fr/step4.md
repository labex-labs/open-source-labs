# Masquez les points

Nous allons masquer les points où y > 0,7 à l'aide d'un tableau masqué. Nous allons créer un nouveau tableau y avec des valeurs masquées.

```python
y3 = np.ma.masked_where(y > 0.7, y)
```
