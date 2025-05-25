# Gerar linhas aleatórias

Geraremos 12 linhas aleatórias usando a biblioteca `numpy` e as plotaremos usando o método `plot`. Se uma linha intersectar o retângulo, sua cor será vermelha, caso contrário, azul. Usaremos a classe `Path` para criar uma linha e o método `intersects_bbox` para verificar se ela intersecta o retângulo.

```python
bbox = Bbox.from_bounds(left, bottom, width, height)

for i in range(12):
    vertices = (np.random.random((2, 2)) - 0.5) * 6.0
    path = Path(vertices)
    if path.intersects_bbox(bbox):
        color = 'r'
    else:
        color = 'b'
    ax.plot(vertices[:, 0], vertices[:, 1], color=color)
```
