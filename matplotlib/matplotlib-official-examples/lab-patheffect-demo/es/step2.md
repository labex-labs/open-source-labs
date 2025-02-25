# Agregar efecto de trazo a texto

Podemos agregar un efecto de trazo a texto utilizando el efecto de ruta `withStroke`. En este ejemplo, agregaremos un efecto de trazo al texto de la anotación en el gráfico.

```python
# Create plot and add text annotation with stroke effect
fig, ax = plt.subplots()
ax.imshow(arr)
txt = ax.annotate("test", (1., 1.), (0., 0),
                   arrowprops=dict(arrowstyle="->",
                                   connectionstyle="angle3", lw=2),
                   size=20, ha="center",
                   path_effects=[patheffects.withStroke(linewidth=3,
                                                        foreground="w")])
txt.arrow_patch.set_path_effects([
    patheffects.Stroke(linewidth=5, foreground="w"),
    patheffects.Normal()])

# Add grid with stroke effect
pe = [patheffects.withStroke(linewidth=3,
                             foreground="w")]
ax.grid(True, linestyle="-", path_effects=pe)

plt.show()
```
