# Crear gráfico

En este paso, creará el gráfico utilizando los datos aleatorios generados anteriormente. En particular, graficará cada punto de datos como un marcador con el símbolo de éxito determinado por la variable de éxito, el tamaño determinado por la variable de habilidad, la rotación determinada por la variable de ángulo de despegue y el color determinado por la variable de fuerza.

```python
fig, ax = plt.subplots()
fig.suptitle("Throwing success", size=14)
for skill, takeoff, thrust, mood, pos in data:
    t = Affine2D().scale(skill).rotate_deg(takeoff)
    m = MarkerStyle(SUCCESS_SYMBOLS[mood], transform=t)
    ax.plot(pos[0], pos[1], marker=m, color=cmap(thrust))
fig.colorbar(plt.cm.ScalarMappable(norm=Normalize(0, 1), cmap=cmap),
             ax=ax, label="Normalized Thrust [a.u.]")
ax.set_xlabel("X position [m]")
ax.set_ylabel("Y position [m]")
```
