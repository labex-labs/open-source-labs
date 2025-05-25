# Adicionar uma elipse ao gráfico

Nesta etapa, adicionaremos uma elipse ao gráfico. Usaremos a função `Ellipse` para criar a elipse e personalizaremos as propriedades da elipse, como a posição, largura, altura e ângulo.

```python
ax = axs.flat[1]
ax.plot([x1, x2], [y1, y2], ".")
el = mpatches.Ellipse((x1, y1), 0.3, 0.4, angle=30, alpha=0.2)
ax.add_artist(el)
```
