# Criar gráfico de violino

Criaremos um gráfico de violino usando o método `violinplot()`. Este método recebe múltiplos argumentos, como dados, showmeans, showmedians, etc.

```python
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))
axs[0].violinplot(all_data, showmeans=False, showmedians=True)
axs[0].set_title('Violin plot')
```
