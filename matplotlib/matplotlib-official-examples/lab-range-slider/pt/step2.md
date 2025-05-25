# Exibir a imagem e seu histograma

Em seguida, exibiremos a imagem usando a função `imshow` do Matplotlib e seu histograma usando `hist`. Criaremos uma figura com dois subplots, um para a imagem e outro para o histograma.

```python
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
fig.subplots_adjust(bottom=0.25)

im = axs[0].imshow(img)
axs[1].hist(img.flatten(), bins='auto')
axs[1].set_title('Histograma das intensidades dos pixels')
```
