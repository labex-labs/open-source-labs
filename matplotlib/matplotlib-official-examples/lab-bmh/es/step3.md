# Crear la gráfica

En este paso, creamos la gráfica llamando a la función `plot_beta_hist()` y pasando los parámetros.

```python
fig, ax = plt.subplots()
plot_beta_hist(ax, 10, 10)
plot_beta_hist(ax, 4, 12)
plot_beta_hist(ax, 50, 12)
plot_beta_hist(ax, 6, 55)
ax.set_title("'bmh' style sheet")

plt.show()
```
