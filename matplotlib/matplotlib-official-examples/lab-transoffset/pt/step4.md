# Adicionar Texto ao Gráfico de Dispersão (Scatter Plot)

Agora adicionaremos texto ao nosso gráfico de dispersão usando `offset_copy`. Primeiro, criaremos uma transformação (transform) que posiciona o texto em um deslocamento (offset) especificado em coordenadas de tela (screen coordinates) em relação a uma localização fornecida em quaisquer coordenadas. Em seguida, usaremos a função `text` de `matplotlib.pyplot` para adicionar o texto ao gráfico.

```python
# Create the transform
trans_offset = mtransforms.offset_copy(ax.transData, fig=fig,
                                       x=0.05, y=0.10, units='inches')

# Add text to the plot
for x, y in zip(xs, ys):
    plt.text(x, y, '%d, %d' % (int(x), int(y)), transform=trans_offset)
```
