# Creando subgráficos sin diseño limitado

Creamos una figura con subgráficos de 2x2 sin utilizar _constrained layout_. Esto resulta en etiquetas solapadas en los ejes.

```python
fig, axs = plt.subplots(nrows=2, ncols=2, layout=None)

for ax in axs.flat:
    example_plot(ax)
```
