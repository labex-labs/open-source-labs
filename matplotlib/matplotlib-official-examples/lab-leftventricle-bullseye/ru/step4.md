# Создание столбчатого графика

Мы создадим столбчатый график с значениями по оси X, меняющимися от 0 до 5, и соответствующими значениями по оси Y. Мы будем использовать функцию `bar`, предоставляемую модулем `pyplot`, для создания столбчатого графика.

```python
# Creating X-axis values
x = np.arange(0, 5, 0.1)

# Creating Y-axis values
y = np.sin(x)

# Creating a bar plot
plt.bar(x, y)

# Adding title and labels to the plot
plt.title('Bar Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Displaying the plot
plt.show()
```
