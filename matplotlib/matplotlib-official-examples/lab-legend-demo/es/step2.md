# Graficar etiquetas más complejas

En este paso, graficaremos etiquetas más complejas.

```python
# Definir los datos para el gráfico
x = np.linspace(0, 1)

# Crear un gráfico con múltiples líneas
fig, (ax0, ax1) = plt.subplots(2, 1)
for n in range(1, 5):
    ax0.plot(x, x**n, label=f"{n=}")

# Crear una leyenda con múltiples columnas y un título
leg = ax0.legend(loc="upper left", bbox_to_anchor=[0, 1],
                 ncols=2, shadow=True, title="Legend", fancybox=True)
leg.get_title().set_color("red")

# Crear un gráfico con múltiples líneas y marcadores
ax1.plot(x, x**2, label="multi\nline")
half_pi = np.linspace(0, np.pi / 2)
ax1.plot(np.sin(half_pi), np.cos(half_pi), label=r"$\frac{1}{2}\pi$")
ax1.plot(x, 2**(x**2), label="$2^{x^2}$")

# Crear una leyenda con una sombra
ax1.legend(shadow=True, fancybox=True)

# Mostrar el gráfico
plt.show()
```
