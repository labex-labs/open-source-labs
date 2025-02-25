# Crear las subtramas

Ahora, crearemos las subtramas utilizando la función `subplots`. Crearemos una cuadrícula de subtramas con la misma relación de aspecto y eliminaremos las marcas de los ejes x e y. También agregaremos una línea vertical y horizontal en el centro de cada subtrama para ayudar a visualizar la alineación.

```python
axs = fig.subplots(len(va_list), len(ha_list), sharex=True, sharey=True,
                   subplot_kw=dict(aspect=1),
                   gridspec_kw=dict(hspace=0, wspace=0))

for i, va in enumerate(va_list):
    for j, ha in enumerate(ha_list):
        ax = axs[i, j]
        ax.set(xticks=[], yticks=[])
        ax.axvline(0.5, color="skyblue", zorder=0)
        ax.axhline(0.5, color="skyblue", zorder=0)
        ax.plot(0.5, 0.5, color="C0", marker="o", zorder=1)
```
