# Создание столбчатой диаграммы

Matplotlib также может создавать столбчатые диаграммы. Вот пример:

```python
x = ['A', 'B', 'C', 'D', 'E']
y = [3, 7, 1, 9, 4]

plt.bar(x, y)
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Plot')
plt.show()
```
