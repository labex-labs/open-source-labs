# Criar Dados

Em seguida, criamos os dados que usaremos em nosso gráfico. Neste exemplo, usaremos NumPy para gerar os dados.

```python
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X ** 2 + Y ** 2))
```
