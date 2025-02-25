# Crear el gráfico

Ahora crearemos el gráfico utilizando las funciones HostAxes y twin() del módulo parasite_axes. HostAxes se utiliza para crear el gráfico principal y twin() se utiliza para crear el eje y secundario.

```python
fig = plt.figure()

# Crear objeto HostAxes
ax_kms = fig.add_subplot(axes_class=HostAxes, aspect=1)

# Crear eje y secundario con coordenadas transformadas
aux_trans = mtransforms.Affine2D().scale(pm_to_kms, 1.)
ax_pm = ax_kms.twin(aux_trans)

# Graficar los datos
for n, ds, dse, w, we in obs:
    time = ((2007 + (10. + 4/30.)/12) - 1988.5)
    v = ds / time * pm_to_kms
    ve = dse / time * pm_to_kms
    ax_kms.errorbar([v], [w], xerr=[ve], yerr=[we], color="k")

# Establecer las etiquetas de los ejes
ax_kms.axis["bottom"].set_label("Velocidad lineal a 2.3 kpc [km/s]")
ax_kms.axis["left"].set_label("FWHM [km/s]")
ax_pm.axis["top"].set_label(r"Movimiento propio [$''$/yr]")

# Ocultar las etiquetas de los ticks en el eje y secundario
ax_pm.axis["right"].major_ticklabels.set_visible(False)

# Establecer los límites del gráfico
ax_kms.set_xlim(950, 3700)
ax_kms.set_ylim(950, 3100)
```
