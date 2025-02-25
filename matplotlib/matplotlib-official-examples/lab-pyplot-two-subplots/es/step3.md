# Crear los subdiagramas

Crearemos una figura con dos subdiagramas utilizando `.pyplot.subplot`.

```python
plt.figure()

plt.subplot(211)
plt.plot(t1, f(t1), color='tab:blue', marker='o')
plt.plot(t2, f(t2), color='black')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), color='tab:orange', linestyle='--')

plt.show()
```

La función `subplot()` toma tres argumentos: el número de filas, el número de columnas y el índice del diagrama actual. El índice comienza en 1 en la esquina superior izquierda y aumenta por filas. En este ejemplo, creamos una figura con dos subdiagramas: uno arriba y uno abajo.

En el primer subdiagrama, graficamos `t1` contra `f(t1)` y `t2` contra `f(t2)`. Establecemos el color de la primera gráfica en azul y agregamos marcadores circulares a cada punto de datos. Establecemos el color de la segunda gráfica en negro.

En el segundo subdiagrama, graficamos `t2` contra la función coseno de `2*np.pi*t2`. Establecemos el color de la gráfica en naranja y el estilo de línea en discontinuo.
