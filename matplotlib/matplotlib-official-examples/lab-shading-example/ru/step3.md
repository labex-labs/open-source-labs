# Создание карты теневой relieve

Теперь мы создадим карту теневой relieve с использованием класса `LightSource`. Мы создадим два подграфика: один с цветовым отображением данных, а другой с интенсивностью освещения.

```python
# Осветить сцену с северо-западного направления
ls = LightSource(azdeg=315, altdeg=45)

fig, axs = plt.subplots(ncols=2, nrows=2)
for ax in axs.flat:
    ax.set(xticks=[], yticks=[])

axs[0, 0].imshow(z, cmap=cmap)
axs[0, 0].set(xlabel='Цветовое отображение данных')

axs[0, 1].imshow(ls.hillshade(z, vert_exag=ve), cmap='gray')
axs[0, 1].set(xlabel='Интенсивность освещения')
```

Мы создадим еще два подграфика: один с `blend_mode` установленным на "hsv", а другой на "overlay".

```python
rgb = ls.shade(z, cmap=cmap, vert_exag=ve, blend_mode='hsv')
axs[1, 0].imshow(rgb)
axs[1, 0].set(xlabel='Режим смешивания: "hsv" (по умолчанию)')

rgb = ls.shade(z, cmap=cmap, vert_exag=ve, blend_mode='overlay')
axs[1, 1].imshow(rgb)
axs[1, 1].set(xlabel='Режим смешивания: "overlay"')
```
