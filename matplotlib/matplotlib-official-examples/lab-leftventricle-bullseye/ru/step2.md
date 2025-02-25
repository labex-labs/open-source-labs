# Создание простого линейного графика

Мы создадим простой линейный график с значениями по оси X, меняющимися от 0 до 5, и соответствующими значениями по оси Y. Мы будем использовать функцию `plot`, предоставляемую модулем `pyplot`, для создания линейного графика.

```python
# Creating X-axis values
x = np.arange(0, 5, 0.1)

# Creating Y-axis values
y = np.sin(x)

# Creating a line plot
plt.plot(x, y)

# Adding title and labels to the plot
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Displaying the plot
plt.show()
```
