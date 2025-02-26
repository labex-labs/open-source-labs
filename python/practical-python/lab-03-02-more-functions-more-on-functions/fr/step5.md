# Retourner des valeurs

L'instruction `return` renvoie une valeur

```python
def square(x):
    return x * x
```

Si aucune valeur de retour n'est donnée ou si `return` est manquant, `None` est renvoyé.

```python
def bar(x):
    statements
    return

a = bar(4)      # a = None

# OU
def foo(x):
    statements  # Pas de `return`

b = foo(4)      # b = None
```
