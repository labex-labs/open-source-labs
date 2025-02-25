# Добавляем таблицу на график

Добавим таблицу в нижнюю часть графика с использованием функции `plt.table`. Передадим в функцию текст ячеек, метки строк, цвета строк и метки столбцов в качестве параметров.

```python
the_table = plt.table(cellText=cell_text,
                      rowLabels=rows,
                      rowColours=colors,
                      colLabels=columns,
                      loc='bottom')
```
