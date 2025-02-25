# Schattierte Reliefplots erstellen

Wir werden nun die schattierten Reliefplots mit der Klasse `LightSource` erstellen. Wir werden zwei Teilplots erstellen, einen mit farbzugeordneten Daten und einen anderen mit Beleuchtungsintensität.

```python
# Beleuchte die Szene aus Nordwesten
ls = LightSource(azdeg=315, altdeg=45)

fig, axs = plt.subplots(ncols=2, nrows=2)
for ax in axs.flat:
    ax.set(xticks=[], yticks=[])

axs[0, 0].imshow(z, cmap=cmap)
axs[0, 0].set(xlabel='Farbzugeordnete Daten')

axs[0, 1].imshow(ls.hillshade(z, vert_exag=ve), cmap='gray')
axs[0, 1].set(xlabel='Beleuchtungsintensität')
```

Wir werden zwei weitere Teilplots erstellen, einen mit `blend_mode` auf "hsv" und einen anderen auf "overlay" gesetzt.

```python
rgb = ls.shade(z, cmap=cmap, vert_exag=ve, blend_mode='hsv')
axs[1, 0].imshow(rgb)
axs[1, 0].set(xlabel='Mischmodus: "hsv" (Standard)')

rgb = ls.shade(z, cmap=cmap, vert_exag=ve, blend_mode='overlay')
axs[1, 1].imshow(rgb)
axs[1, 1].set(xlabel='Mischmodus: "overlay"')
```
