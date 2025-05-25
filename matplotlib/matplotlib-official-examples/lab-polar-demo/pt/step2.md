# Gerar os dados

Em seguida, precisamos gerar os dados para o gráfico de linha. Usaremos a biblioteca `numpy` para gerar um array de valores para `r` e `theta`.

```python
r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r
```
