# Creando subgráficos con diseño limitado

Creamos los mismos subgráficos de 2x2, pero esta vez utilizamos _constrained layout_. Esto ajusta automáticamente los subgráficos para evitar solapes entre los objetos de los ejes y las etiquetas.

```python
fig, axs = plt.subplots(nrows=2, ncols=2, layout='constrained')

for ax in axs.flat:
    example_plot(ax)
```
