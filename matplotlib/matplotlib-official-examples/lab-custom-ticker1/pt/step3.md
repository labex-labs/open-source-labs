# Criar o Gráfico

Agora, podemos criar o gráfico com o ticker personalizado. Criaremos um gráfico de barras com dados de exemplo e definiremos o ticker do eixo y para usar nossa função de ticker personalizado.

```python
# Create a bar chart with sample data
fig, ax = plt.subplots()
money = [1.5e5, 2.5e6, 5.5e6, 2.0e7]
ax.bar(['Bill', 'Fred', 'Mary', 'Sue'], money)

# Set the y-axis ticker to use the custom ticker function
ax.yaxis.set_major_formatter(ticker.FuncFormatter(millions))

# Display the plot
plt.show()
```
