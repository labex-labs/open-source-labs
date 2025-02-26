# Возвращение к исключениям

В упражнениях мы написали функцию `parse()`, которая выглядела примерно так:

```python
# fileparse.py
def parse(f, types=None, names=None, delimiter=None):
    records = []
    for line in f:
        line = line.strip()
        if not line: continue
        try:
            records.append(split(line,types,names,delimiter))
        except ValueError as e:
            print("Couldn't parse :", line)
            print("Reason :", e)
    return records
```

Обратите внимание на инструкцию `try-except`. Что нужно делать в блоке `except`?

Следует ли выводить сообщение об ошибке?

```python
try:
    records.append(split(line,types,names,delimiter))
except ValueError as e:
    print("Couldn't parse :", line)
    print("Reason :", e)
```

Или тихо игнорировать его?

```python
try:
    records.append(split(line,types,names,delimiter))
except ValueError as e:
    pass
```

Ни одно из решений не является удовлетворительным, потому что часто требуются _оба_ поведения (возможность выбора пользователем).
