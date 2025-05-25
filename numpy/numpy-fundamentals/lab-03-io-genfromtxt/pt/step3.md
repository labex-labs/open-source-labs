# Dividindo as Linhas em Colunas

O argumento `delimiter` é usado para definir como as linhas devem ser divididas em colunas. Por padrão, `numpy.genfromtxt` assume `delimiter=None`, o que significa que a linha é dividida ao longo dos espaços em branco (incluindo tabulações).

```python
np.genfromtxt(StringIO(data), delimiter=",")
```
