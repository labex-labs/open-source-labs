# Módulos e importación

Cualquier archivo fuente de Python es un módulo.

```python
# foo.py
def grok(a):
 ...
def spam(b):
 ...
```

La declaración `import` carga y _ejecuta_ un módulo.

```python
# program.py
import foo

a = foo.grok(2)
b = foo.spam('Hello')
...
```
