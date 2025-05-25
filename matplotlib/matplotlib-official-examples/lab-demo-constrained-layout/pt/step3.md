# Criando Subplots Sem Constrained Layout

Criamos uma figura com subplots 2x2 sem usar _constrained layout_. Isso resulta em rótulos sobrepostos nos eixos.

```python
fig, axs = plt.subplots(nrows=2, ncols=2, layout=None)

for ax in axs.flat:
    example_plot(ax)
```
