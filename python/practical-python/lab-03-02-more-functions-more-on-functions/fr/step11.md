# Passage d'arguments

Lorsque vous appelez une fonction, les variables d'arguments sont des noms qui se réfèrent aux valeurs passées. Ces valeurs ne sont PAS des copies. Si des types de données mutables sont passés (par exemple, des listes, des dictionnaires), ils peuvent être modifiés _in-place_.

```python
def foo(items):
    items.append(42)    # Modifie l'objet d'entrée

a = [1, 2, 3]
foo(a)
print(a)                # [1, 2, 3, 42]
```

**Point clé : Les fonctions ne reçoivent pas une copie des arguments d'entrée.**
