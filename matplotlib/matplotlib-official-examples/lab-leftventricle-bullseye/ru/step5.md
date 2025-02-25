# Создание круговой диаграммы

Мы создадим круговую диаграмму с пятью сегментами, представляющими разные данные. Мы будем использовать функцию `pie`, предоставляемую модулем `pyplot`, для создания круговой диаграммы.

```python
# Creating data for the pie chart
data = [10, 20, 30, 25, 15]

# Creating labels for the pie chart
labels = ['Data 1', 'Data 2', 'Data 3', 'Data 4', 'Data 5']

# Creating a pie chart
plt.pie(data, labels=labels)

# Adding title to the plot
plt.title('Pie Chart')

# Displaying the plot
plt.show()
```
