# Создание столбчатой диаграммы с несколькими видами штриховки

Вы также можете использовать несколько видов штриховки в своей столбчатой диаграмме. В данном случае мы будем использовать массив штриховок, чтобы создать несколько видов штриховки на наших столбцах.

```python
plt.bar(x, y1, edgecolor='black', hatch=['--', '+', 'x', '\\'])
plt.bar(x, y2, bottom=y1, edgecolor='black', hatch=['*', 'o', 'O', '.'])
```
