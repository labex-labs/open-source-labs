# Criar dados para o gráfico de superfície

Nesta etapa, criaremos dados para o gráfico de superfície. Criaremos uma malha (meshgrid) de valores X e Y, calcularemos a distância radial R e calcularemos o valor Z com base no valor R usando `np.sin()`.

```python
# Create data for the surface plot
X = np.arange(-5, 5, 0.25)
xlen = len(X)
Y = np.arange(-5, 5, 0.25)
ylen = len(Y)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
```
