# Модули и импорт

Любой исходный файл на Python является модулем.

```python
# foo.py
def grok(a):
 ...
def spam(b):
 ...
```

Инструкция `import` загружает и _исполняет_ модуль.

```python
# program.py
import foo

a = foo.grok(2)
b = foo.spam('Hello')
...
```
