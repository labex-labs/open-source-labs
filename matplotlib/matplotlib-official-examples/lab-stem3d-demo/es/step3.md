# Crear el diagrama de tallos tridimensional

En este paso, crearemos el diagrama de tallos tridimensional utilizando la función `stem` de Matplotlib. Pasaremos las coordenadas x, y y z como argumentos a la función `stem`.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
ax.stem(x, y, z)

plt.show()
```
