# Validation (Redux)

Dans l'exercice précédent, vous avez écrit un décorateur `@validated` qui imposait les annotations de type. Par exemple :

```python
@validated
def add(x: Integer, y:Integer) -> Integer:
    return x + y
```

Créez un nouveau décorateur `@enforce()` qui impose les types spécifiés via des arguments clés au décorateur à la place. Par exemple :

```python
@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x + y
```

Le comportement résultant de la fonction décorée devrait être identique. Note : Utilisez le mot clé `return_` pour spécifier le type de retour. `return` est un mot réservé en Python, donc vous devez choisir un nom légèrement différent.

**Discussion**

Écrire des décorateurs robustes est souvent beaucoup plus difficile qu'il n'y paraît. Lecture recommandée :
