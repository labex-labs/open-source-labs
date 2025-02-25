# Créer un diagramme en violon

Nous allons créer un diagramme en violon à l'aide de la méthode `violinplot()`. Cette méthode prend plusieurs arguments tels que les données, showmeans, showmedians, etc.

```python
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))
axs[0].violinplot(all_data, showmeans=False, showmedians=True)
axs[0].set_title('Violin plot')
```
