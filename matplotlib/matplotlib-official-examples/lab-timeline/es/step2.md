# Creando un diagrama de tallos

A continuación, crearemos un diagrama de tallos con algunas variaciones en los niveles para distinguir incluso eventos cercanos. Agregamos marcadores en la línea base para enfatizar visualmente la naturaleza unidimensional de la cronología. Para cada evento, agregamos una etiqueta de texto a través de `~.Axes.annotate`, que está desplazada en unidades de puntos desde la punta de la línea del evento. Aquí está el código para crear un diagrama de tallos:

```python
# Choose some nice levels
levels = np.tile([-5, 5, -3, 3, -1, 1],
                 int(np.ceil(len(dates)/6)))[:len(dates)]

# Create figure and plot a stem plot with the date
fig, ax = plt.subplots(figsize=(8.8, 4), layout="constrained")
ax.set(title="Matplotlib release dates")

ax.vlines(dates, 0, levels, color="tab:red")  # The vertical stems.
ax.plot(dates, np.zeros_like(dates), "-o",
        color="k", markerfacecolor="w")  # Baseline and markers on it.

# annotate lines
for d, l, r in zip(dates, levels, names):
    ax.annotate(r, xy=(d, l),
                xytext=(-3, np.sign(l)*3), textcoords="offset points",
                horizontalalignment="right",
                verticalalignment="bottom" if l > 0 else "top")
```
