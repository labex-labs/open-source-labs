# Форматирование словаря

Вы можете использовать метод `format_map()` для применения форматирования строк к словарю значений:

```python
>>> s = {
    'name': 'IBM',
   'shares': 100,
    'price': 91.1
}
>>> '{name:>10s} {shares:10d} {price:10.2f}'.format_map(s)
'       IBM        100      91.10'
>>>
```

Он использует те же коды, что и `f-строки`, но берет значения из предоставленного словаря.
