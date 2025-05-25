# Criar cores para o gráfico de superfície

Nesta etapa, criaremos cores para o gráfico de superfície. Criaremos um array vazio de strings com a mesma forma da malha (meshgrid) e o preencheremos com duas cores em um padrão quadriculado (checkerboard).

```python
# Create colors for the surface plot
colortuple = ('y', 'b')
colors = np.empty(X.shape, dtype=str)
for y in range(ylen):
    for x in range(xlen):
        colors[y, x] = colortuple[(x + y) % len(colortuple)]
```
