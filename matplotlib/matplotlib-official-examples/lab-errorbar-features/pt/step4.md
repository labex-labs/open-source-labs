# Plotar Variável, Barras de Erro Simétricas

Agora plotaremos nossos dados com barras de erro variáveis e simétricas. A função `ax.errorbar()` é usada para criar o gráfico, e o parâmetro `yerr` é usado para especificar os valores de erro.

```python
# plot variable, symmetric error bars
fig, ax = plt.subplots()
ax.errorbar(x, y, yerr=error, fmt='-o')
ax.set_title('Variable, Symmetric Error Bars')
plt.show()
```
