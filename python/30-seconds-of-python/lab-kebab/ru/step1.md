# Строка в стиле kebab case

Напишите функцию на Python под названием `to_kebab_case(s)`, которая принимает на вход строку `s` и возвращает версию строки в стиле kebab case. Функция должна выполнять следующие шаги:

1. Замените любые `-` или `_` на пробел, используя регулярное выражение `r"(_|-)+"`.
2. Найдите все слова в строке и приведите их к нижнему регистру с помощью `str.lower()`.
3. Объедините все слова, используя `-` в качестве разделителя.

```python
from re import sub

def kebab(s):
  return '-'.join(
    sub(r"(\s|_|-)+"," ",
    sub(r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+",
    lambda mo: ' ' + mo.group(0).lower(), s)).split())
```

```python
kebab('camelCase') # 'camel-case'
kebab('some text') # 'some-text'
kebab('some-mixed_string With spaces_underscores-and-hyphens')
# 'some-mixed-string-with-spaces-underscores-and-hyphens'
kebab('AllThe-small Things') # 'all-the-small-things'
```
