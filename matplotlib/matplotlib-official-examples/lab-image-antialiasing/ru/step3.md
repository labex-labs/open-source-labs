# Десэмплирование изображения с использованием интерполяции "antialiased"

Далее мы уменьшим разрешение изображения от 450 пикселей до 125 или 250 пикселей с использованием интерполяции "antialiased". Это покажет, как антиалиасинг может быть использован для уменьшения эффекта Моира, вызываемого уменьшением разрешения высокочастотных данных.

```python
fig, axs = plt.subplots(2, 2, figsize=(5, 6), layout='constrained')
axs[0, 0].imshow(a, interpolation='nearest', cmap='RdBu_r')
axs[0, 0].set_xlim(100, 200)
axs[0, 0].set_ylim(275, 175)
axs[0, 0].set_title('Zoom')

for ax, interp, space in zip(axs.flat[1:],
                             ['nearest', 'antialiased', 'antialiased'],
                             ['data', 'data', 'rgba']):
    ax.imshow(a, interpolation=interp, interpolation_stage=space,
              cmap='RdBu_r')
    ax.set_title(f"interpolation='{interp}'\nspace='{space}'")
plt.show()
```
