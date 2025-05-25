# Box Plot Padrão

Começaremos criando um box plot padrão para visualizar os dados. Usaremos a função Matplotlib `boxplot()` e passaremos os dados e os rótulos como argumentos. Também definiremos o título do gráfico usando a função `set_title()`.

```python
fig, ax = plt.subplots()
ax.boxplot(data, labels=labels)
ax.set_title('Default Box Plot')
plt.show()
```
