# Définitions globales

Tout ce qui est défini dans l'espace de portée _globale_ est ce qui remplit l'espace de noms du module. Considérez deux modules qui définissent la même variable `x`.

```python
# foo.py
x = 42
def grok(a):
 ...
```

```python
# bar.py
x = 37
def spam(a):
 ...
```

Dans ce cas, les définitions de `x` se réfèrent à des variables différentes. L'une est `foo.x` et l'autre est `bar.x`. Différents modules peuvent utiliser les mêmes noms et ces noms ne se conflitent pas les uns avec les autres.

**Les modules sont isolés.**
