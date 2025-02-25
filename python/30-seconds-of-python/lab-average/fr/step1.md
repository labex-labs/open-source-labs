# Moyenne

Écrivez une fonction appelée `average` qui prend deux nombres ou plus en entrée et renvoie leur moyenne. Votre fonction doit suivre les directives suivantes :

- Utilisez `sum()` pour additionner tous les `args` fournis, puis divisez par `len()`.
- La fonction doit être capable de gérer un nombre quelconque d'arguments.
- La fonction doit renvoyer un nombre à virgule flottante.

```python
def average(*args):
  return sum(args, 0.0) / len(args)
```

```python
average(*[1, 2, 3]) # 2.0
average(1, 2, 3) # 2.0
```
