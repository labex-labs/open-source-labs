# Definir como NaN

Definiremos como NaN onde y > 0.7. Criaremos um novo array y com valores NaN.

```python
y4 = y.copy()
y4[y3 > 0.7] = np.nan
```
