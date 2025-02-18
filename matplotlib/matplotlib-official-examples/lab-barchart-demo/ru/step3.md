# Определение вспомогательных функций

Мы определяем две вспомогательные функции. Первая функция, `to_ordinal`, преобразует целое число в порядковое числительное в виде строки (например, 2 -> '2nd'). Вторая функция, `format_score`, создает метки для правой оси y в виде названия теста, за которым следует единица измерения (если она есть), разделенные на две строки.

```python
def to_ordinal(num):
    suffixes = {str(i): v
                for i, v in enumerate(['th', 'st', 'nd', 'rd', 'th',
                                       'th', 'th', 'th', 'th', 'th'])}
    v = str(num)
    if v in {'11', '12', '13'}:
        return v + 'th'
    return v + suffixes[v[-1]]

def format_score(score):
    return f'{score.value}\n{score.unit}' if score.unit else str(score.value)
```
