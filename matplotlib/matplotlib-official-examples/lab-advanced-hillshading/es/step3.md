# Mostrando diferentes variables a través del sombreado y el color

En este paso, aprenderás a mostrar diferentes variables a través del sombreado y el color.

```python
def shade_other_data():
    """Demuestra la visualización de diferentes variables a través del sombreado y el color."""
    y, x = np.mgrid[-4:2:200j, -4:2:200j]
    z1 = np.sin(x**2)  # Datos para el sombreado de relieve
    z2 = np.cos(x**2 + y**2)  # Datos para el color

    norm = Normalize(z2.min(), z2.max())
    cmap = plt.cm.RdBu

    ls = LightSource(315, 45)
    rgb = ls.shade_rgb(cmap(norm(z2)), z1)

    fig, ax = plt.subplots()
    ax.imshow(rgb, interpolation='bilinear')
    ax.set_title('Shade by one variable, color by another', size='x-large')
```
