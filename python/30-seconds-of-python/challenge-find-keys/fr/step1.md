# Trouver les clés avec une valeur donnée

## Problème

Écrivez une fonction Python appelée `trouver_cles(dictionnaire, valeur)` qui prend un dictionnaire et une valeur en arguments et renvoie une liste de toutes les clés dans le dictionnaire qui ont la valeur donnée. Si aucune clé n'a la valeur donnée, la fonction devrait renvoyer une liste vide.

Pour résoudre ce problème, vous pouvez utiliser la méthode `dictionnaire.items()`, qui renvoie un générateur qui produit des paires clé-valeur du dictionnaire. Vous pouvez ensuite utiliser une compréhension de liste pour filtrer les clés qui ont la valeur donnée.

## Exemple

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 10,
}
trouver_cles(ages, 10) # [ 'Peter', 'Anna' ]
```

Dans cet exemple, la fonction `trouver_cles()` est appelée avec un dictionnaire `ages` et une valeur `10`. La fonction renvoie une liste de clés qui ont la valeur `10`, qui sont `'Peter'` et `'Anna'`.
