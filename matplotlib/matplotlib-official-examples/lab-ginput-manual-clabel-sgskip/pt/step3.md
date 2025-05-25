# Zoom

Nesta etapa, faremos zoom no gráfico. Usaremos a função `ginput` para selecionar dois cantos da caixa de zoom e a função `waitforbuttonpress` para finalizar o zoom.

```python
tellme('Agora faça um zoom aninhado, clique para começar')
plt.waitforbuttonpress()

while True:
    tellme('Selecione dois cantos do zoom, botão do meio do mouse para finalizar')
    pts = plt.ginput(2, timeout=-1)
    if len(pts) < 2:
        break
    (x0, y0), (x1, y1) = pts
    xmin, xmax = sorted([x0, x1])
    ymin, ymax = sorted([y0, y1])
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)

tellme('Tudo Feito!')
plt.show()
```
