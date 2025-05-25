# Criar um gráfico

Em seguida, criaremos um gráfico usando a função `imshow` do Matplotlib. Esta função exibe uma imagem no gráfico. Também criaremos uma figura com dois subplots.

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.subplots_adjust(wspace=0.5)

im1 = ax1.imshow([[1, 2], [3, 4]])

im2 = ax2.imshow([[1, 2], [3, 4]])
```
