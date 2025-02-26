# Décorateurs

Mettre des wrappers autour de fonctions est extrêmement courant en Python. Tellement courant qu'il existe une syntaxe spéciale pour cela.

```python
def add(x, y):
    return x + y
add = logged(add)

# Syntaxe spéciale
@logged
def add(x, y):
    return x + y
```

La syntaxe spéciale effectue exactement les mêmes étapes que celles montrées ci-dessus. Un décorateur n'est qu'une nouvelle syntaxe. On dit qu'il _décore_ la fonction.
