# Criar o histograma preenchido com hachuras e rotulado

Criaremos um histograma preenchido com hachuras e rotulado usando a função `stack_hist` que definimos anteriormente. Usaremos os `dict_data`, `color_cycle` e `hist_func` que definimos anteriormente. Também definiremos `labels` para `['set 0', 'set 3']` para plotar apenas o primeiro e o último conjunto.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5), tight_layout=True, sharey=True)
dict_data = dict(zip((c['label'] for c in label_cycle), stack_data))
arts = stack_hist(ax1, dict_data, color_cycle + hatch_cycle, hist_func=hist_func)

arts = stack_hist(ax2, dict_data, color_cycle + hatch_cycle, hist_func=hist_func, labels=['set 0', 'set 3'])
ax1.xaxis.set_major_locator(mticker.MaxNLocator(5))
ax1.set_xlabel('contagens')
ax1.set_ylabel('x')
ax2.set_ylabel('x')
```
