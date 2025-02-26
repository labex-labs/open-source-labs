# Modules

Tout fichier source Python est un module.

```python
# foo.py
def grok(a):
  ...
def spam(b):
  ...
```

Une instruction `import` charge et _exécute_ un module.

```python
# program.py
import foo

a = foo.grok(2)
b = foo.spam('Hello')
...
```
