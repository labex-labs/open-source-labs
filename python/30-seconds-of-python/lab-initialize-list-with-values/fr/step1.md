# Initialiser une liste avec des valeurs

Écrivez une fonction `initialiser_liste_avec_valeurs(n, val=0)` qui prend deux paramètres :

- `n` (entier) représentant la longueur de la liste à créer.
- `val` (entier) représentant la valeur à utiliser pour remplir la liste. Si `val` n'est pas fourni, la valeur par défaut `0` doit être utilisée.

La fonction doit renvoyer une liste de longueur `n` remplie avec la valeur spécifiée.

```python
def initialiser_liste_avec_valeurs(n, val = 0):
  return [val for x in range(n)]
```

```python
initialiser_liste_avec_valeurs(5, 2) # [2, 2, 2, 2, 2]
```
