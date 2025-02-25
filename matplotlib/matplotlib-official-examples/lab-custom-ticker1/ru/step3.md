# Создаем график

Теперь мы можем создать график с использованием пользовательского индикатора цен. Мы создадим столбчатую диаграмму с примерами данных и настроим деления по оси y на использование нашей функции пользовательского индикатора цен.

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
