# Criar um gráfico de violino padrão

Em seguida, criaremos um gráfico de violino padrão usando a função `violinplot` do Matplotlib. Isso fornecerá uma linha de base para comparação quando personalizarmos o gráfico em etapas posteriores.

```python
# create default violin plot
fig, ax1 = plt.subplots()
ax1.set_title('Default Violin Plot')
ax1.set_ylabel('Observed Values')
ax1.violinplot(data)
```
