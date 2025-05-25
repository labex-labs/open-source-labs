# Usar Transparência para Destacar Valores

Finalmente, recriaremos o mesmo gráfico, mas desta vez usaremos a transparência para destacar os valores extremos nos dados. Isso é frequentemente usado para destacar pontos de dados com valores p menores. Também adicionaremos linhas de contorno para destacar os valores da imagem.

```python
# Create an alpha channel based on weight values
alphas = Normalize(0, .3, clip=True)(np.abs(weights))
alphas = np.clip(alphas, .4, 1)  # alpha value clipped at the bottom at .4

# Create the figure and image
fig, ax = plt.subplots()
ax.imshow(greys)
ax.imshow(weights, alpha=alphas, **imshow_kwargs)

# Add contour lines to further highlight different levels.
ax.contour(weights[::-1], levels=[-.1, .1], colors='k', linestyles='-')
ax.set_axis_off()
plt.show()

ax.contour(weights[::-1], levels=[-.0001, .0001], colors='k', linestyles='-')
ax.set_axis_off()
plt.show()
```
