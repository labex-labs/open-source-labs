# Строка в snake case

## Задача

Напишите функцию на Python под названием `snake`, которая принимает строку в качестве аргумента и возвращает строку в snake case. Функция должна выполнять следующие шаги:

1. Используйте `re.sub()`, чтобы найти все слова в строке, а затем `str.lower()`, чтобы привести их к нижнему регистру.
2. Используйте `re.sub()`, чтобы заменить все символы `-` на пробелы.
3. Наконец, используйте `str.join()`, чтобы объединить все слова с использованием `_` в качестве разделителя.

Ваша функция должна уметь обрабатывать строки, содержащие смесь заглавных и строчных букв, пробелы, дефисы и нижние подчеркивания.

## Пример

```python
snake('camelCase') # 'camel_case'
snake('some text') # 'some_text'
snake('some-mixed_string With spaces_underscores-and-hyphens')
# 'some_mixed_string_with_spaces_underscores_and_hyphens'
snake('AllThe-small Things') # 'all_the_small_things'
```
