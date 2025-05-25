# Criar Arrays Mascarados

Nesta etapa, criaremos três arrays mascarados: um para valores maiores que um determinado limite (threshold), um para valores menores que um determinado limite e um para valores entre dois limites.

```python
upper = 0.77
lower = -0.77

supper = np.ma.masked_where(s < upper, s)
slower = np.ma.masked_where(s > lower, s)
smiddle = np.ma.masked_where((s < lower) | (s > upper), s)
```
