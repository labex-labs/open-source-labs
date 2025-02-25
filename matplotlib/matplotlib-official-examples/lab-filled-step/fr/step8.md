# Créez l'histogramme avec des hachures et des étiquettes

Nous allons créer un histogramme avec des hachures et des étiquettes en utilisant la fonction `stack_hist` que nous avons définie précédemment. Nous allons utiliser les `dict_data`, `color_cycle` et `hist_func` que nous avons définis précédemment. Nous allons également définir `labels` sur `['ensemble 0', 'ensemble 3']` pour tracer seulement le premier et le dernier ensemble.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5), tight_layout=True, sharey=True)
dict_data = dict(zip((c['label'] for c in label_cycle), stack_data))
arts = stack_hist(ax1, dict_data, color_cycle + hatch_cycle, hist_func=hist_func)

arts = stack_hist(ax2, dict_data, color_cycle + hatch_cycle, hist_func=hist_func, labels=['ensemble 0', 'ensemble 3'])
ax1.xaxis.set_major_locator(mticker.MaxNLocator(5))
ax1.set_xlabel('comptes')
ax1.set_ylabel('x')
ax2.set_ylabel('x')
```
