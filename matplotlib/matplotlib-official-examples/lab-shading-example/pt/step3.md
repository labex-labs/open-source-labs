# Criar Gráficos de Relevo Sombreado

Agora criaremos os gráficos de relevo sombreado usando a classe `LightSource`. Criaremos dois subplots, um com dados mapeados por cores e o outro com intensidade de iluminação.

```python
# Illuminate the scene from the northwest
ls = LightSource(azdeg=315, altdeg=45)

fig, axs = plt.subplots(ncols=2, nrows=2)
for ax in axs.flat:
    ax.set(xticks=[], yticks=[])

axs[0, 0].imshow(z, cmap=cmap)
axs[0, 0].set(xlabel='Colormapped Data')

axs[0, 1].imshow(ls.hillshade(z, vert_exag=ve), cmap='gray')
axs[0, 1].set(xlabel='Illumination Intensity')
```

Criaremos mais dois subplots, um com o `blend_mode` definido como "hsv" e o outro como "overlay".

```python
rgb = ls.shade(z, cmap=cmap, vert_exag=ve, blend_mode='hsv')
axs[1, 0].imshow(rgb)
axs[1, 0].set(xlabel='Blend Mode: "hsv" (default)')

rgb = ls.shade(z, cmap=cmap, vert_exag=ve, blend_mode='overlay')
axs[1, 1].imshow(rgb)
axs[1, 1].set(xlabel='Blend Mode: "overlay"')
```
