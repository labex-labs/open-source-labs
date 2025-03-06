# Обработка более сложных шаблонов

Наша текущая функция работает для camelCase, но нам нужно улучшить ее, чтобы она могла обрабатывать дополнительные шаблоны, такие как:

1. PascalCase (например, `HelloWorld`)
2. Строки с дефисами (например, `hello-world`)
3. Строки, которые уже содержат подчеркивания (например, `hello_world`)

Давайте обновим нашу функцию, чтобы она могла обрабатывать эти случаи:

```python
import re

def snake(s):
    # Replace hyphens with spaces
    s = s.replace('-', ' ')

    # Handle PascalCase pattern (sequences of uppercase letters)
    s = re.sub('([A-Z]+)', r' \1', s)

    # Handle camelCase pattern (lowercase followed by uppercase)
    s = re.sub('([a-z])([A-Z])', r'\1 \2', s)

    # Split by spaces, join with underscores, and convert to lowercase
    return '_'.join(s.split()).lower()

# Test with multiple examples
if __name__ == "__main__":
    test_strings = [
        "helloWorld",
        "HelloWorld",
        "hello-world",
        "hello_world",
        "some text"
    ]

    for test in test_strings:
        result = snake(test)
        print(f"Original: {test}")
        print(f"Snake case: {result}")
        print("-" * 20)
```

Улучшения, которые мы внесли:

1. Сначала мы заменяем все дефисы на пробелы.
2. Новое регулярное выражение `re.sub('([A-Z]+)', r' \1', s)` добавляет пробел перед любой последовательностью заглавных букв, что помогает обработать PascalCase.
3. Мы сохраняем наше регулярное выражение для обработки camelCase.
4. Наконец, мы разбиваем строку по пробелам, объединяем ее с использованием подчеркиваний и преобразуем в нижний регистр, что позволяет обработать любые оставшиеся пробелы и обеспечить последовательный вывод.

Запустите скрипт, чтобы протестировать его с различными форматами входных данных:

```bash
python3 ~/project/snake_case.py
```

Вы должны увидеть вывод, похожий на следующий:

```
Original: helloWorld
Snake case: hello_world
--------------------
Original: HelloWorld
Snake case: hello_world
--------------------
Original: hello-world
Snake case: hello_world
--------------------
Original: hello_world
Snake case: hello_world
--------------------
Original: some text
Snake case: some_text
--------------------
```

Наша функция теперь более надежная и может обрабатывать различные форматы входных данных. На следующем шаге мы внесем последние усовершенствования и протестируем ее на полном наборе тестов.
