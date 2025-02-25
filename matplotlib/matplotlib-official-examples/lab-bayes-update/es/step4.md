# Crear la animación

Ahora que hemos definido la clase `UpdateDist`, podemos crear la animación utilizando la clase `FuncAnimation` de Matplotlib. Creamos un objeto de figura y un objeto de eje y pasamos el objeto de eje a la clase `UpdateDist` para crear una nueva instancia de la clase.

```python
fig, ax = plt.subplots()
ud = UpdateDist(ax, prob=0.7)
anim = FuncAnimation(fig, ud, frames=100, interval=100, blit=True)
plt.show()
```

La clase `FuncAnimation` toma varios argumentos:

- `fig`: el objeto de figura
- `ud`: la instancia de `UpdateDist`
- `frames`: el número de fotogramas para animar
- `interval`: el tiempo entre fotogramas en milisegundos
- `blit`: si se debe actualizar solo las partes del gráfico que han cambiado
