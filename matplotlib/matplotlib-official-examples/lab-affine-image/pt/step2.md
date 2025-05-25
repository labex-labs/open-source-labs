# Criar uma Função para Plotar a Imagem

Nesta etapa, definimos uma função que recebe a imagem, o eixo do gráfico e a transformação como entradas. A função exibe a imagem no eixo do gráfico com a transformação especificada. A função também exibe um retângulo amarelo ao redor da imagem para mostrar a extensão pretendida da imagem.

```python
def do_plot(ax, Z, transform):
    im = ax.imshow(Z, interpolation='none',
                   origin='lower',
                   extent=[-2, 4, -3, 2], clip_on=True)

    trans_data = transform + ax.transData
    im.set_transform(trans_data)

    # display intended extent of the image
    x1, x2, y1, y2 = im.get_extent()
    ax.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1], "y--",
            transform=trans_data)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-4, 4)
```
