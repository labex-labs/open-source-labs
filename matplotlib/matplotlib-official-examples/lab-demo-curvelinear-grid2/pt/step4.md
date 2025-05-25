# Definir Eixos e Exibir Imagem

O quarto passo é definir os eixos usando a instância `grid_helper` criada no Passo 3. Também exibiremos uma imagem usando a função `imshow`.

```python
ax1 = fig.add_subplot(axes_class=Axes, grid_helper=grid_helper)
ax1.imshow(np.arange(25).reshape(5, 5), vmax=50, cmap=plt.cm.gray_r, origin="lower")
```
