# Criar o Gráfico

Criamos uma grade de gráfico 4x3 para mostrar os gráficos com sombreamento (hillshaded) com diferentes modos de mistura (blend modes) e exagero vertical. Primeiro, mostramos a imagem de intensidade do sombreamento na primeira linha e, em seguida, colocamos gráficos com sombreamento com diferentes modos de mistura no restante das linhas. Usamos um loop `for` para iterar pelos diferentes valores de exagero vertical e modos de mistura.

```python
fig, axs = plt.subplots(nrows=4, ncols=3, figsize=(8, 9))
plt.setp(axs.flat, xticks=[], yticks=[])

for col, ve in zip(axs.T, [0.1, 1, 10]):
    col[0].imshow(ls.hillshade(z, vert_exag=ve, dx=dx, dy=dy), cmap='gray')
    for ax, mode in zip(col[1:], ['hsv', 'overlay', 'soft']):
        rgb = ls.shade(z, cmap=cmap, blend_mode=mode,
                       vert_exag=ve, dx=dx, dy=dy)
        ax.imshow(rgb)
```
