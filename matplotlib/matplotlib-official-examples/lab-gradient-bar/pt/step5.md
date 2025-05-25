# Criar o gráfico

Agora, podemos criar o gráfico. Primeiro, criaremos uma figura e um objeto de eixos (axes). Em seguida, definiremos os limites x e y dos eixos. Criaremos um fundo gradiente usando a função `gradient_image()`. Finalmente, criaremos um conjunto de dados aleatórios e usaremos a função `gradient_bar()` para criar o gráfico de barras.

```python
fig, ax = plt.subplots()
ax.set(xlim=(0, 10), ylim=(0, 1))

# background image
gradient_image(ax, direction=1, extent=(0, 1, 0, 1), transform=ax.transAxes,
               cmap=plt.cm.RdYlGn, cmap_range=(0.2, 0.8), alpha=0.5)

N = 10
x = np.arange(N) + 0.15
y = np.random.rand(N)
gradient_bar(ax, x, y, width=0.7)
plt.show()
```
