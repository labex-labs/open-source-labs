# Crear diagrama de violín

Crearemos un diagrama de violín utilizando el método `violinplot()`. Este método toma múltiples argumentos como datos, mostrar medias, mostrar medianas, etc.

```python
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))
axs[0].violinplot(all_data, showmeans=False, showmedians=True)
axs[0].set_title('Violin plot')
```
