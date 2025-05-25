# Criar Barras de Erro Theta Sobrepostas

Nesta etapa, criaremos barras de erro theta sobrepostas para demonstrar como elas podem reduzir a legibilidade do gráfico de saída.

```python
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection='polar')
ax.errorbar(theta, r, xerr=5.25, yerr=0.1, capsize=7, fmt="o", c="darkred")
ax.set_title("Overlapping Theta Error Bars")
plt.show()
```
