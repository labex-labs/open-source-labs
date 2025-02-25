# Aplicando TickedStroke a los gráficos de contorno

En este paso, aplicaremos TickedStroke a los gráficos de contorno.

```python
fig, ax = plt.subplots(figsize=(6, 6))

nx = 101
ny = 105

# Establece los vectores de la encuesta
xvec = np.linspace(0.001, 4.0, nx)
yvec = np.linspace(0.001, 4.0, ny)

# Establece las matrices de la encuesta. Diseña la carga del disco y la relación de transmisión.
x1, x2 = np.meshgrid(xvec, yvec)

# Evalúa algunas cosas para graficar
obj = x1**2 + x2**2 - 2*x1 - 2*x2 + 2
g1 = -(3*x1 + x2 - 5.5)
g2 = -(x1 + 2*x2 - 4.5)
g3 = 0.8 + x1**-3 - x2

cntr = ax.contour(x1, x2, obj, [0.01, 0.1, 0.5, 1, 2, 4, 8, 16],
                  colors='black')
ax.clabel(cntr, fmt="%2.1f", use_clabeltext=True)

cg1 = ax.contour(x1, x2, g1, [0], colors='sandybrown')
plt.setp(cg1.collections,
         path_effects=[patheffects.withTickedStroke(angle=135)])

cg2 = ax.contour(x1, x2, g2, [0], colors='orangered')
plt.setp(cg2.collections,
         path_effects=[patheffects.withTickedStroke(angle=60, length=2)])

cg3 = ax.contour(x1, x2, g3, [0], colors='mediumblue')
plt.setp(cg3.collections,
         path_effects=[patheffects.withTickedStroke(spacing=7)])

ax.set_xlim(0, 4)
ax.set_ylim(0, 4)

plt.show()
```

Este código creará un gráfico de contorno con el efecto de ruta TickedStroke.
