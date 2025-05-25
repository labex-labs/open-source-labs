# Criar Dados para Visualização

Em seguida, criaremos uma grade 2D que usaremos para visualização. Podemos criar uma grade usando a função `meshgrid` em NumPy. A função `meshgrid` cria uma grade de pontos dados dois vetores, `x` e `y`, que representam as coordenadas dos pontos da grade. Criaremos uma grade de 5x5 pontos usando o seguinte bloco de código:

```python
nrows = 5
ncols = 5
x = np.arange(ncols + 1)
y = np.arange(nrows + 1)
X, Y = np.meshgrid(x, y)
Z = X + Y
```
