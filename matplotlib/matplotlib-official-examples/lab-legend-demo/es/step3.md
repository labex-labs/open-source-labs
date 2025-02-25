# Adjuntar leyendas a gráficos más complejos

En este paso, adjuntaremos leyendas a gráficos más complejos.

```python
# Definir los datos para el gráfico
fig, axs = plt.subplots(3, 1, layout="constrained")
top_ax, middle_ax, bottom_ax = axs

# Crear un gráfico de barras con múltiples barras
top_ax.bar([0, 1, 2], [0.2, 0.3, 0.1], width=0.4, label="Barra 1",
           align="center")
top_ax.bar([0.5, 1.5, 2.5], [0.3, 0.2, 0.2], color="rojo", width=0.4,
           label="Barra 2", align="center")
top_ax.legend()

# Crear un gráfico de barras de error con múltiples errores
middle_ax.errorbar([0, 1, 2], [2, 3, 1], xerr=0.4, fmt="s", label="prueba 1")
middle_ax.errorbar([0, 1, 2], [3, 2, 4], yerr=0.3, fmt="o", label="prueba 2")
middle_ax.errorbar([0, 1, 2], [1, 1, 3], xerr=0.4, yerr=0.3, fmt="^",
                   label="prueba 3")
middle_ax.legend()

# Crear un gráfico de tallo con una leyenda
bottom_ax.stem([0.3, 1.5, 2.7], [1, 3.6, 2.7], label="prueba de tallo")
bottom_ax.legend()

# Mostrar el gráfico
plt.show()
```
