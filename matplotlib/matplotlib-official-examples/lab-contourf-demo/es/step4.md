# Establecer la paleta de colores y la configuración de extensión

Finalmente, estableceremos la paleta de colores y la configuración de extensión. Usaremos el método `with_extremes` para establecer los colores para los valores por debajo y por encima del rango de niveles. También crearemos cuatro subgráficos para mostrar los cuatro posibles ajustes de `extend`: `'neither'`, `'both'`, `'min'` y `'max'`.

```python
# Establecer la paleta de colores y la configuración de extensión
extends = ["neither", "both", "min", "max"]
cmap = plt.colormaps["winter"].with_extremes(under="magenta", over="yellow")

# Crear subgráficos con diferentes configuraciones de extensión
fig, axs = plt.subplots(2, 2, layout="constrained")
for ax, extend in zip(axs.flat, extends):
    cs = ax.contourf(X, Y, Z, levels, cmap=cmap, extend=extend, origin=origin)
    fig.colorbar(cs, ax=ax, shrink=0.9)
    ax.set_title("extend = %s" % extend)
    ax.locator_params(nbins=4)

# Mostrar el gráfico
plt.show()
```
