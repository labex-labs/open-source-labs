# Adicionando Texto ao Gráfico

Podemos adicionar texto ao gráfico usando a função `ax.text()`. Esta função recebe três argumentos: a coordenada x, a coordenada y e a string de texto. Podemos personalizar o estilo do texto usando os argumentos `style`, `bbox` e `fontsize`.

```python
ax.text(3, 8, 'boxed italics text in data coords', style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

ax.text(2, 6, r'an equation: $E=mc^2$', fontsize=15)

ax.text(3, 2, 'Unicode: Institut f\374r Festk\366rperphysik')

ax.text(0.95, 0.01, 'colored text in axes coords',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='green', fontsize=15)
```
