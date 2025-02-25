# Преобразовать первую букву строки в строчную

Напишите функцию `decapitalize(s, upper_rest = False)`, которая принимает строку `s` и возвращает новую строку с первой буквой в нижнем регистре. Функция также должна иметь необязательный параметр `upper_rest`, который, когда равен `True`, переводит остальную часть строки в верхний регистр.

```python
def decapitalize(s, upper_rest = False):
  return ''.join([s[:1].lower(), (s[1:].upper() if upper_rest else s[1:])])
```

```python
decapitalize('FooBar') # 'fooBar'
decapitalize('FooBar', True) # 'fOOBAR'
```
