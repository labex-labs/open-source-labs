# Создание точечного графика

Кроме линейных графиков, Matplotlib также позволяет нам создавать точечные графики. Точечные графики полезны для визуализации взаимосвязи между двумя переменными.

```python
# Create the data
x = np.random.rand(50)
y = np.random.rand(50)

# Create the scatter plot
plt.scatter(x, y)

# Add title and axis labels
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()
```
