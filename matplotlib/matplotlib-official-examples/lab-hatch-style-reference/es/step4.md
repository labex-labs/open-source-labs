# Crear el primer conjunto de patrones de sombreado

Crearemos el primer conjunto de patrones de sombreado utilizando la siguiente lista:

```python
hatches = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']
```

Luego utilizaremos un bucle para crear un rectángulo con cada patrón de sombreado y agregarlo a un subgráfico.

```python
for ax, h in zip(axs.flat, hatches):
    hatches_plot(ax, h)
```
