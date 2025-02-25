# Перевести строку в верхний регистр

Напишите функцию на Python под названием `capitalize_string(s, lower_rest=False)`, которая принимает строку в качестве аргумента и возвращает новую строку с первой буквой в верхнем регистре. Функция должна иметь необязательный параметр `lower_rest`, который, если установить в `True`, переводит остальную часть строки в нижний регистр.

```python
def capitalize(s, lower_rest = False):
  return ''.join([s[:1].upper(), (s[1:].lower() if lower_rest else s[1:])])
```

```python
capitalize('fooBar') # 'FooBar'
capitalize('fooBar', True) # 'Foobar'
```
