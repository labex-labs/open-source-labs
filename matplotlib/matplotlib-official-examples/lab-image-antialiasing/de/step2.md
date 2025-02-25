# Bild mit 'nearest' Interpolation unterabtasten

Nun werden wir das Bild von 450 Datenpunkten auf 125 oder 250 Pixel unterabtasten, indem wir 'nearest' Interpolation verwenden. Dies wird demonstrieren, wie die Unterabtastung von Hochfrequenzdaten Moiré-Muster verursachen kann.

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
