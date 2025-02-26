# Module

Jede Python-Quelldatei ist ein Modul.

```python
# foo.py
def grok(a):
 ...
def spam(b):
 ...
```

Eine `import`-Anweisung lädt und _führt_ ein Modul aus.

```python
# program.py
import foo

a = foo.grok(2)
b = foo.spam('Hello')
...
```
