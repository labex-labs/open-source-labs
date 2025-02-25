# Создание точечного графика

Мы создадим точечный график с значениями по оси X, меняющимися от 0 до 5, и соответствующими значениями по оси Y. Мы будем использовать функцию `scatter`, предоставляемую модулем `pyplot`, для создания точечного графика.

```python
# Creating X-axis values
x = np.arange(0, 5, 0.1)

# Creating Y-axis values
y = np.sin(x)

# Creating a scatter plot
plt.scatter(x, y)

# Adding title and labels to the plot
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Displaying the plot
plt.show()
```
