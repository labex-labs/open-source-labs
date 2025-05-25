# Criar o Gráfico de Barras

O próximo passo é criar o gráfico de barras. Usaremos a função `bar()` para criar o gráfico. Criaremos dois conjuntos de barras, um para chá e outro para café. Também adicionaremos barras de erro ao gráfico.

```python
ax.bar(ind, tea_means, width, bottom=0*cm, yerr=tea_std, label='Tea')
ax.bar(ind + width, coffee_means, width, bottom=0*cm, yerr=coffee_std,
       label='Coffee')
```
