# Adicionar patches e anotações de dica de ferramenta

Em seguida, adicionamos os patches e as anotações de dica de ferramenta ao gráfico. As anotações de dica de ferramenta são criadas usando o método `annotate`. Definimos o parâmetro `xy` para as coordenadas do patch e `xytext` para `(0, 0)` para posicionar a dica de ferramenta diretamente sobre o patch. Também definimos o parâmetro `textcoords` para `'offset points'` para alinhar a dica de ferramenta com o patch. Definimos o parâmetro `color` para `'w'` para tornar o texto branco, `ha` para `'center'` para centralizar o texto horizontalmente, `fontsize` para `8` para definir o tamanho da fonte e `bbox` para definir o estilo da caixa da dica de ferramenta.

```python
for i, (item, label) in enumerate(zip(shapes, labels)):
    patch = ax.add_patch(item)
    annotate = ax.annotate(labels[i], xy=item.get_xy(), xytext=(0, 0),
                           textcoords='offset points', color='w', ha='center',
                           fontsize=8, bbox=dict(boxstyle='round, pad=.5',
                                                 fc=(.1, .1, .1, .92),
                                                 ec=(1., 1., 1.), lw=1,
                                                 zorder=1))

    ax.add_patch(patch)
    patch.set_gid(f'mypatch_{i:03d}')
    annotate.set_gid(f'mytooltip_{i:03d}')
```
