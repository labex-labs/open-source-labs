# Gerar Dados

Em seguida, precisamos gerar alguns dados para usar em nosso gráfico de hastes. Criaremos dois arrays usando a biblioteca Numpy.

```python
x = np.linspace(0.1, 2 * np.pi, 41)
y = np.exp(np.sin(x))
```
