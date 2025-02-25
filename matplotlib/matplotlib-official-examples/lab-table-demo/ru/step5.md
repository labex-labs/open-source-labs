# Создаем вертикальную накопленную столбчатую диаграмму

Создадим вертикальную накопленную столбчатую диаграмму с использованием функции `plt.bar`, чтобы представить убытки, понесенные различными природными катастрофами за годы. Используем цикл for для перебора каждой строки данных и построения столбцов.

```python
n_rows = len(data)

index = np.arange(len(columns)) + 0.3
bar_width = 0.4

y_offset = np.zeros(len(columns))

cell_text = []
for row in range(n_rows):
    plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
    y_offset = y_offset + data[row]
    cell_text.append(['%1.1f' % (x / 1000.0) for x in y_offset])
```
