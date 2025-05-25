# Adicionando Linhas de Grade Horizontais

Finalmente, adicionaremos linhas de grade horizontais aos gráficos de caixa usando a função `yaxis.grid()`.

```python
for ax in [ax1, ax2]:
    ax.yaxis.grid(True)
    ax.set_xlabel('Three Separate Samples')
    ax.set_ylabel('Observed Values')

plt.show()
```
