# Submuestrear imagen con interpolación 'antialiased'

A continuación, submuestreamos la imagen de 450 píxeles de datos a 125 píxeles o 250 píxeles utilizando interpolación 'antialiased'. Esto demostrará cómo se puede utilizar el anti-aliasing para reducir los patrones de Moiré causados por la submuestreación de datos de alta frecuencia.

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
    ax.set_title(f"interpolación='{interp}'\nespacio='{space}'")
plt.show()
```
