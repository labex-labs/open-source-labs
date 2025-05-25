# Criar a figura e configurar os eixos

Em seguida, criaremos uma figura e configuraremos os eixos. Usaremos o método `add_axes()` para criar um novo conjunto de eixos dentro da figura. Também definiremos limites para os eixos x e y e adicionaremos linhas de grade.

```python
# Create figure and axes
fig = plt.figure(figsize=(7.5, 7.5))
ax = fig.add_axes([0.2, 0.17, 0.68, 0.7], aspect=1)

# Set limits and gridlines
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)
```
