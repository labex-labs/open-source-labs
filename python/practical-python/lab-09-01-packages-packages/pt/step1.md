# Módulos (Modules)

Qualquer arquivo fonte Python é um módulo.

```python
# foo.py
def grok(a):
    ...
def spam(b):
    ...
```

Uma declaração `import` carrega e _executa_ um módulo.

```python
# program.py
import foo

a = foo.grok(2)
b = foo.spam('Hello')
...
```
