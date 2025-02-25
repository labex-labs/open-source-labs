# Personalizar y guardar el gráfico

Podemos personalizar aún más el gráfico utilizando las opciones de personalización de Matplotlib. También podemos guardar el gráfico en un archivo.

```python
# Personalizando y guardando el gráfico
fig, axs = plt.subplots(figsize=(12, 4))
air_quality.plot.area(ax=axs)
axs.set_ylabel("Concentración de NO$_2$")
fig.savefig("no2_concentraciones.png")
plt.show()
```
