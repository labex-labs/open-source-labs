# Rellenando regiones horizontales de forma selectiva

El parámetro _where_ permite especificar los rangos de x que se deben rellenar. Es una matriz booleana del mismo tamaño que _x_. Solo se rellenan los rangos de x de secuencias contiguas de valores _True_. Como resultado, el rango entre valores _True_ y _False_ adyacentes nunca se rellena. Por lo tanto, se recomienda establecer `interpolate=True` a menos que la distancia en x de los puntos de datos sea lo suficientemente fina para que el efecto anterior no sea notable.

```python
x = np.array([0, 1, 2, 3])
y1 = np.array([0.8, 0.8, 0.2, 0.2])
y2 = np.array([0, 0, 1, 1])

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

ax1.set_title('interpolación=False')
ax1.plot(x, y1, 'o--')
ax1.plot(x, y2, 'o--')
ax1.fill_between(x, y1, y2, donde=(y1 > y2), color='C0', alpha=0.3)
ax1.fill_between(x, y1, y2, donde=(y1 < y2), color='C1', alpha=0.3)

ax2.set_title('interpolación=True')
ax2.plot(x, y1, 'o--')
ax2.plot(x, y2, 'o--')
ax2.fill_between(x, y1, y2, donde=(y1 > y2), color='C0', alpha=0.3,
                 interpolación=True)
ax2.fill_between(x, y1, y2, donde=(y1 <= y2), color='C1', alpha=0.3,
                 interpolación=True)
fig.tight_layout()
```
