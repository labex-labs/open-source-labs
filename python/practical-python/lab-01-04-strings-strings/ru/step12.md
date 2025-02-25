# Упражнение 1.13: Извлечение отдельных символов и подстрок

Строки - это массивы символов. Попробуйте извлечь несколько символов:

```python
>>> symbols[0]
?
>>> symbols[1]
?
>>> symbols[2]
?
>>> symbols[-1]        # Последний символ
?
>>> symbols[-2]        # Отрицательные индексы отсчитываются от конца строки
?
>>>
```

В Python строки являются неизменяемыми (read-only).

Проверьте это, попробовав изменить первый символ `symbols` на строчную 'a'.

```python
>>> symbols[0] = 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>>
```
