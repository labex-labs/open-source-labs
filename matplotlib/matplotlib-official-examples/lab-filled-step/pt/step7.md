# Criar o histograma preenchido com hachuras

Criaremos um histograma preenchido com hachuras usando a função `stack_hist` que definimos anteriormente. Usaremos os `stack_data`, `color_cycle` e `hist_func` que definimos anteriormente. Também definiremos `plot_kwargs` para incluir `edgecolor` e `orientation`.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5), tight_layout=True)
arts = stack_hist(ax1, stack_data, color_cycle + label_cycle + hatch_cycle, hist_func=hist_func)

arts = stack_hist(ax2, stack_data, color_cycle, hist_func=hist_func, plot_kwargs=dict(edgecolor='w', orientation='h'))
ax1.set_ylabel('contagens')
ax1.set_xlabel('x')
ax2.set_xlabel('contagens')
ax2.set_ylabel('x')
```
