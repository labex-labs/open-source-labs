# Преобразование строки в snake case

Напишите функцию на Python с именем `snake`, которая принимает строку в качестве аргумента и возвращает строку в формате "snake case" (змеиный регистр). Функция должна выполнять следующие шаги:

1. Используйте `re.sub()`, чтобы найти все слова в строке, а затем примените `str.lower()`, чтобы преобразовать их в нижний регистр.
2. Используйте `re.sub()`, чтобы заменить все символы `-` на пробелы.
3. Наконец, используйте `str.join()`, чтобы объединить все слова, используя `_` в качестве разделителя.

Ваша функция должна уметь обрабатывать строки, содержащие смесь заглавных и строчных букв, пробелы, дефисы и подчеркивания.

```python
from re import sub

def snake(s):
  return '_'.join(
    sub('([A-Z][a-z]+)', r' \1',
    sub('([A-Z]+)', r' \1',
    s.replace('-', ' '))).split()).lower()
```

```python
snake('camelCase') # 'camel_case'
snake('some text') # 'some_text'
snake('some-mixed_string With spaces_underscores-and-hyphens')
# 'some_mixed_string_with_spaces_underscores_and_hyphens'
snake('AllThe-small Things') # 'all_the_small_things'
```
