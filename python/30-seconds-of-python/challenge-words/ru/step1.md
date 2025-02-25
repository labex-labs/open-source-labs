# Задача по преобразованию строки в слова

## Задача

Напишите функцию `string_to_words(s: str, pattern: str = '[a-zA-Z-]+') -> List[str]`, которая принимает строку `s` и необязательную строку `pattern` в качестве аргументов и возвращает список слов в строке.

- Функция должна использовать `re.findall()` с заданным `pattern` для нахождения всех совпадающих подстрок.
- Если аргумент `pattern` не указан, функция должна использовать стандартное регулярное выражение, которое соответствует буквенно-цифровым символам и дефисам.

## Пример

```python
string_to_words('I love Python!!') # ['I', 'love', 'Python']
string_to_words('python, javaScript & coffee') # ['python', 'javaScript', 'coffee']
string_to_words('build -q --out one-item', r'\b[a-zA-Z-]+\b') # ['build', 'q', 'out', 'one-item']
```
