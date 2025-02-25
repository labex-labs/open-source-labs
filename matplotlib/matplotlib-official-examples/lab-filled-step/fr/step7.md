# Créez l'histogramme avec des hachures

Nous allons créer un histogramme avec des hachures en utilisant la fonction `stack_hist` que nous avons définie précédemment. Nous allons utiliser les `stack_data`, `color_cycle` et `hist_func` que nous avons définis précédemment. Nous allons également définir `plot_kwargs` pour inclure la couleur de bord et l'orientation.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5), tight_layout=True)
arts = stack_hist(ax1, stack_data, color_cycle + label_cycle + hatch_cycle, hist_func=hist_func)

arts = stack_hist(ax2, stack_data, color_cycle, hist_func=hist_func, plot_kwargs=dict(edgecolor='w', orientation='h'))
ax1.set_ylabel('comptes')
ax1.set_xlabel('x')
ax2.set_xlabel('comptes')
ax2.set_ylabel('x')
```
