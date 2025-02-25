# Crear una animación

Creamos una animación utilizando la clase `FuncAnimation` de `matplotlib.animation`. Pasamos el objeto de figura, la función de actualización, el número total de fotogramas (que es igual al número de pasos en los paseos aleatorios), la lista de todos los paseos aleatorios y la lista de todas las líneas como argumentos al constructor de `FuncAnimation`.

```python
# Creating the Animation object
ani = animation.FuncAnimation(
    fig, update_lines, num_steps, fargs=(walks, lines), interval=100)
```
