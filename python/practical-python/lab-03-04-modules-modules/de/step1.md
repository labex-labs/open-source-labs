# Module und Import

Jede Python-Quelldatei ist ein Modul.

```python
# foo.py
def grok(a):
 ...
def spam(b):
 ...
```

Die `import`-Anweisung lädt und _führt aus_ ein Modul aus.

```python
# program.py
import foo

a = foo.grok(2)
b = foo.spam('Hello')
...
```
