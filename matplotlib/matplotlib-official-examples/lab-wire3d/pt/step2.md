# Gerar Dados

Em seguida, geraremos os dados que usaremos para criar o gráfico de wireframe. Neste laboratório, usaremos a função `np.meshgrid()` para criar as coordenadas X, Y e Z.

```python
# Generate data
X, Y = np.meshgrid(np.arange(-5, 5, 0.25), np.arange(-5, 5, 0.25))
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
```
