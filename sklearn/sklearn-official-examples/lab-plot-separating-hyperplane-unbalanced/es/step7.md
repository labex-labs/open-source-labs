# Agregar leyenda

Vamos a agregar una leyenda a la gráfica utilizando la función `legend` de `matplotlib.pyplot`. Estableceremos las etiquetas en `"no ponderado"` y `"ponderado"`, respectivamente.

```python
plt.legend(
    [disp.surface_.collections[0], wdisp.surface_.collections[0]],
    ["non weighted", "weighted"],
    loc="upper right",
)
```
