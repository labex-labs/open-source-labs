# Crear el segundo conjunto de patrones de sombreado

Crearemos el segundo conjunto de patrones de sombreado repitiendo cada patrón dos veces para aumentar la densidad. Utilizaremos la siguiente lista:

```python
hatches = ['//', '\\\\', '||', '--', '++', 'xx', 'oo', 'OO', '..', '**']
```

Utilizaremos el mismo bucle que antes para crear los rectángulos.

```python
for ax, h in zip(axs.flat, hatches):
    hatches_plot(ax, h)
```
