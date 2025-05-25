# Criando Subplots Com Constrained Layout

Criamos os mesmos subplots 2x2, mas desta vez usamos _constrained layout_. Isso ajusta automaticamente os subplots para evitar sobreposições entre objetos de eixos e rótulos.

```python
fig, axs = plt.subplots(nrows=2, ncols=2, layout='constrained')

for ax in axs.flat:
    example_plot(ax)
```
