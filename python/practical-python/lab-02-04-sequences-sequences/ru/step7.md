# continue - оператор

Для пропуска одного элемента и перехода к следующему используйте оператор `continue`.

```python
for line in lines:
    if line == '\n':    # Пропустить пустые строки
        continue
    # Дальнейшие инструкции
 ...
```

Это полезно, когда текущий элемент не представляет интерес или должен быть проигнорирован при обработке.
