# Criando um Gráfico de Barras

Outro tipo comum de gráfico é o gráfico de barras (bar chart). Gráficos de barras são úteis para comparar os valores de diferentes categorias.

```python
# Create the data
x = ['A', 'B', 'C', 'D', 'E']
y = [3, 7, 1, 9, 4]

# Create the bar chart
plt.bar(x, y)

# Add title and axis labels
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

plt.show()
```
