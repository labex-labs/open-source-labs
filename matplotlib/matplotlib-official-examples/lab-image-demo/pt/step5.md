# Controlar a origem da imagem

```python
# Especificar se as imagens devem ser plotadas com a origem do array x[0, 0] no canto superior esquerdo ou inferior direito
x = np.arange(120).reshape((10, 12))

interp = 'bilinear'
fig, axs = plt.subplots(nrows=2, sharex=True, figsize=(3, 5))
axs[0].set_title('azul deve estar em cima')
axs[0].imshow(x, origin='upper', interpolation=interp)

axs[1].set_title('azul deve estar em baixo')
axs[1].imshow(x, origin='lower', interpolation=interp)
plt.show()
```
