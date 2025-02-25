# Crear el tercer conjunto de patrones de sombreado

Crearemos el tercer conjunto de patrones de sombreado combinando dos patrones para crear uno nuevo. Utilizaremos la siguiente lista:

```python
hatches = ['/o', '\\|', '|*', '-\\', '+o', 'x*', 'o-', 'O|', 'O.', '*-']
```

Utilizaremos el mismo bucle que antes para crear los rectángulos.

```python
for ax, h in zip(axs.flat, hatches):
    hatches_plot(ax, h)
```
