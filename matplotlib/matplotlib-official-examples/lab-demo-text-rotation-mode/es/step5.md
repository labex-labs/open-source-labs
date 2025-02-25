# Agregar texto a las subtramas

Agregaremos texto a cada subtrama utilizando la función `text`. Usaremos los parámetros `rotation` (rotación), `horizontalalignment` (alineación horizontal), `verticalalignment` (alineación vertical) y `rotation_mode` (modo de rotación) para rotar y alinear el texto. También usaremos el parámetro `bbox` (caja delimitadora) para resaltar la caja delimitadora del texto.

```python
kw = (
    {} if mode == "default" else
    {"bbox": dict(boxstyle="square,pad=0.", ec="none", fc="C1", alpha=0.3)}
)

texts = {}

for i, va in enumerate(va_list):
    for j, ha in enumerate(ha_list):
        ax = axs[i, j]
        tx = ax.text(0.5, 0.5, "Tpg",
                     size="x-large", rotation=40,
                     horizontalalignment=ha, verticalalignment=va,
                     rotation_mode=mode, **kw)
        texts[ax] = tx
```
