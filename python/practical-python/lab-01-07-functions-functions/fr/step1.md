# Fonctions personnalisées

Utilisez des fonctions pour le code que vous voulez réutiliser. Voici une définition de fonction :

```python
def sumcount(n):
    '''
    Renvoie la somme des n premiers entiers
    '''
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total
```

Pour appeler une fonction.

```python
a = sumcount(100)
```

Une fonction est une série d'instructions qui effectuent une certaine tâche et renvoient un résultat. Le mot clé `return` est nécessaire pour spécifier explicitement la valeur de retour de la fonction.
