# Crear el diagrama SkewT-logP

Ahora crearemos el diagrama SkewT-logP utilizando la proyección SkewXAxes que registramos anteriormente. Primero crearemos un objeto de figura y agregaremos un subgráfico con la proyección SkewXAxes. Luego graficaremos los datos de temperatura y punto de rocío en el diagrama utilizando la función semilogy. Finalmente, estableceremos los límites y las marcas de graduación para los ejes X e Y y mostraremos la gráfica.

```python
fig = plt.figure(figsize=(6.5875, 6.2125))
ax = fig.add_subplot(projection='skewx')

ax.semilogy(T, p, color='C3')
ax.semilogy(Td, p, color='C2')

ax.axvline(0, color='C0')

ax.yaxis.set_major_formatter(ScalarFormatter())
ax.yaxis.set_minor_formatter(NullFormatter())
ax.set_yticks(np.linspace(100, 1000, 10))
ax.set_ylim(1050, 100)

ax.xaxis.set_major_locator(MultipleLocator(10))
ax.set_xlim(-50, 50)

plt.grid(True)
plt.show()
```
