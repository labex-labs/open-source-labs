# Обработка исключений

Исключения распространяются до первого совпадающего `except`.

```python
def grok():
  ...
    raise RuntimeError('Whoa!')   # Исключение возникает здесь

def spam():
    grok()                        # Вызов, который вызовет исключение

def bar():
    try:
       spam()
    except RuntimeError as e:     # Исключение поймано здесь
      ...

def foo():
    try:
         bar()
    except RuntimeError as e:     # Исключение НЕ приходит сюда
      ...

foo()
```

Для обработки исключения поместите инструкции в блок `except`. Вы можете добавить любые инструкции, чтобы обработать ошибку.

```python
def grok():...
    raise RuntimeError('Whoa!')

def bar():
    try:
      grok()
    except RuntimeError as e:   # Исключение поймано здесь
        statements              # Используйте эти инструкции
        statements
     ...

bar()
```

После обработки выполнение продолжается с первой инструкции после `try-except`.

```python
def grok():...
    raise RuntimeError('Whoa!')

def bar():
    try:
      grok()
    except RuntimeError as e:   # Исключение поймано здесь
        statements
        statements
     ...
    statements                  # Продолжает выполнение здесь
    statements                  # И продолжает здесь
 ...

bar()
```
