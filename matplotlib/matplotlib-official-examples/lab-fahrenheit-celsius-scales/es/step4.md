# Crear la gráfica

Ahora, creamos una gráfica con dos ejes y utilizando la función `subplots()` de `matplotlib.pyplot`. También conectamos el evento `ylim_changed` del primer eje a la función `convert_ax_c_to_celsius()`.

```python
fig, ax_f = plt.subplots()
ax_c = ax_f.twinx()

ax_f.callbacks.connect("ylim_changed", convert_ax_c_to_celsius)
```
