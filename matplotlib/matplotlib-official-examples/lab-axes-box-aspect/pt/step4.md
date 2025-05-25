# Gráfico Normal ao Lado de uma Imagem

Ao criar um gráfico de imagem com aspecto de dados fixo e o padrão `adjustable="box"` ao lado de um gráfico normal, os eixos teriam alturas desiguais. `set_box_aspect()` fornece uma solução fácil para isso, permitindo que os eixos do gráfico normal usem as dimensões das imagens como aspecto da caixa (box aspect). Este exemplo também mostra que o _layout restrito_ (constrained layout) interage bem com um aspecto de caixa fixo.

```python
fig4, (ax, ax2) = plt.subplots(ncols=2, layout="constrained")

np.random.seed(19680801)  # Fixing random state for reproducibility
im = np.random.rand(16, 27)
ax.imshow(im)

ax2.plot([23, 45])
ax2.set_box_aspect(im.shape[0]/im.shape[1])

plt.show()
```
