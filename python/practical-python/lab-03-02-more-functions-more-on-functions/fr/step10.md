# Modifier les variables globales

Si vous devez modifier une variable globale, vous devez la déclarer comme telle.

```python
name = 'Dave'

def spam():
    global name
    name = 'Guido' # Modifie la variable globale name ci-dessus
```

La déclaration `global` doit apparaître avant son utilisation et la variable correspondante doit exister dans le même fichier que la fonction. Ayant vu cela, sachez que cela est considéré comme une mauvaise pratique. En fait, essayez d'éviter complètement `global` si vous le pouvez. Si vous avez besoin qu'une fonction modifie un certain type d'état en dehors de la fonction, il est préférable d'utiliser une classe à la place (nous en reparlerons plus tard).
