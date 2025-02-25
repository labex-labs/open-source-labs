# Map List to Dictionary

## Problème

Écrivez une fonction Python appelée `map_dictionary(itr, fn)` qui prend deux paramètres :

- `itr` : une liste de valeurs
- `fn` : une fonction qui prend une valeur en entrée et renvoie une valeur en sortie

La fonction devrait renvoyer un dictionnaire où les paires clé-valeur sont composées de la valeur d'origine comme clé et du résultat de la fonction comme valeur.

Pour résoudre ce problème, suivez ces étapes :

1. Utilisez `map()` pour appliquer `fn` à chaque valeur de la liste.
2. Utilisez `zip()` pour associer les valeurs d'origine aux valeurs produites par `fn`.
3. Utilisez `dict()` pour renvoyer un dictionnaire approprié.

## Exemple

```python
map_dictionary([1, 2, 3], lambda x: x * x) # { 1: 1, 2: 4, 3: 9 }
```

Dans cet exemple, la fonction `map_dictionary()` prend une liste `[1, 2, 3]` et une fonction lambda `lambda x: x * x` en entrée. La fonction lambda calcule le carré de la valeur d'entrée. La fonction renvoie un dictionnaire `{ 1: 1, 2: 4, 3: 9 }` où les clés sont les valeurs d'origine de la liste et les valeurs sont les carrés des valeurs.
