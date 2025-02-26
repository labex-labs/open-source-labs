# Définition de fonction

Les fonctions peuvent être _définies_ dans n'importe quel ordre.

```python
def foo(x):
    bar(x)

def bar(x):
    instructions

# OU
def bar(x):
    instructions

def foo(x):
    bar(x)
```

Les fonctions doivent seulement être définies avant d'être réellement _utilisées_ (ou appelées) pendant l'exécution du programme.

```python
foo(3)        # foo doit déjà être définie
```

Du point de vue de la présentation, il est probablement plus courant de voir les fonctions définies de manière _du bas vers le haut_.
