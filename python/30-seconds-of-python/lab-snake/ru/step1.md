# Понимание проблемы

Прежде чем мы напишем функцию для преобразования в snake case, давайте разберемся, что нам нужно сделать:

1. Мы должны преобразовать строку из любого формата в snake case.
2. Snake case означает, что все буквы должны быть в нижнем регистре, а слова разделены подчеркиваниями.
3. Мы должны обрабатывать различные форматы входных данных:
   - camelCase (например, `camelCase` → `camel_case`)
   - Строки с пробелами (например, `some text` → `some_text`)
   - Строки с смешанным форматированием (например, с дефисами, подчеркиваниями и смешанным регистром)

Начнем с создания нового файла Python для нашей функции snake case. В WebIDE перейдите в директорию проекта и создайте новый файл с именем `snake_case.py`:

```python
# This function will convert a string to snake case
def snake(s):
    # We'll implement this function step by step
    pass  # Placeholder for now

# Test with a simple example
if __name__ == "__main__":
    test_string = "helloWorld"
    result = snake(test_string)
    print(f"Original: {test_string}")
    print(f"Snake case: {result}")
```

Сохраните этот файл. На следующем шаге мы начнем реализацию функции.

Пока что давайте запустим нашу заглушку функции, чтобы убедиться, что наш файл настроен правильно. Откройте терминал и запустите:

```bash
python3 ~/project/snake_case.py
```

![python-prompt](../assets/screenshot-20250306-B5lI9tyo@2x.png)

Вы должны увидеть вывод, похожий на следующий:

```
Original: helloWorld
Snake case: None
```

Результат равен `None`, потому что наша функция в настоящее время просто возвращает значение по умолчанию Python `None`. На следующем шаге мы добавим фактическую логику преобразования.
