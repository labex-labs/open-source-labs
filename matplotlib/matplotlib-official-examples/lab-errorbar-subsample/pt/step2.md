# Plotar Todas as Barras de Erro

Em seguida, plotaremos todas as barras de erro usando a função `errorbar` sem qualquer subamostragem. Isso servirá como nosso gráfico de linha de base.

```python
fig, ax = plt.subplots()

ax.set_title('Todas as Barras de Erro')
ax.errorbar(x, y1, yerr=y1err, label='y1')
ax.errorbar(x, y2, yerr=y2err, label='y2')

ax.legend()
plt.show()
```
