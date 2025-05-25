# Plotando o Padrão de Esparsidade

Usaremos a função `spy` para plotar o padrão de esparsidade (sparsity pattern) do array. Usaremos diferentes parâmetros como `markersize` e `precision` para personalizar o gráfico.

```python
ax1.spy(x, markersize=5)
ax2.spy(x, precision=0.1, markersize=5)
ax3.spy(x)
ax4.spy(x, precision=0.1)
```
