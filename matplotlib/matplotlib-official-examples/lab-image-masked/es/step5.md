# Creando un gráfico de barras

Otro tipo común de gráfico es el gráfico de barras. Los gráficos de barras son útiles para comparar los valores de diferentes categorías.

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
