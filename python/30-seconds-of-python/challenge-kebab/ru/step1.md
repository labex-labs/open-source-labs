# Строка в стиле kebab case

## Задача

Напишите функцию на Python под названием `to_kebab_case(s)`, которая принимает на вход строку `s` и возвращает версию строки в стиле kebab case. Функция должна выполнять следующие шаги:

1. Замените любые `-` или `_` на пробел, используя регулярное выражение `r"(_|-)+"`.
2. Найдите все слова в строке и приведите их к нижнему регистру с помощью `str.lower()`.
3. Объедините все слова, используя `-` в качестве разделителя.

## Пример

```python
to_kebab_case('camelCase') # 'camel-case'
to_kebab_case('some text') # 'some-text'
to_kebab_case('some-mixed_string With spaces_underscores-and-hyphens')
# 'some-mixed-string-with-spaces-underscores-and-hyphens'
to_kebab_case('AllThe-small Things') # 'all-the-small-things'
```
