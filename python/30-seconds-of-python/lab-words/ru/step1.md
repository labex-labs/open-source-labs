# Преобразование строки в слова

Напишите функцию `string_to_words(s: str, pattern: str = '[a-zA-Z-]+') -> List[str]`, которая принимает на вход строку `s` и необязательную строку `pattern` и возвращает список слов в строке.

- Функция должна использовать `re.findall()` с заданным `pattern` для нахождения всех совпадающих подстрок.
- Если аргумент `pattern` не указан, функция должна использовать стандартное регулярное выражение, которое соответствует буквенно-цифровым символам и дефисам.

```python
import re

def words(s, pattern = '[a-zA-Z-]+'):
  return re.findall(pattern, s)
```

```python
words('I love Python!!') # ['I', 'love', 'Python']
words('python, javaScript & coffee') # ['python', 'javaScript', 'coffee']
words('build -q --out one-item', r'\b[a-zA-Z-]+\b')
# ['build', 'q', 'out', 'one-item']
```
