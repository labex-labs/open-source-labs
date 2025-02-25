# Listes de niveaux d'arbre

## Problème

Étant donné un arbre de recherche binaire, créer une liste pour chaque niveau de l'arbre. Chaque liste devrait contenir les nœuds de ce niveau de l'arbre. Les listes devraient être retournées dans un tableau de tableaux, où chaque sous-tableau représente un niveau de l'arbre.

## Exigences

Pour résoudre ce problème, les exigences suivantes doivent être satisfaites :

- L'arbre donné est un arbre de recherche binaire.
- Chaque niveau de l'arbre devrait être représenté par une liste de nœuds.
- Une classe `Node` avec une méthode `insert` est déjà fournie.
- La solution devrait tenir en mémoire.

## Utilisation de l'exemple

Par exemple, étant donné l'arbre de recherche binaire avec les valeurs suivantes :

```
5, 3, 8, 2, 4, 1, 7, 6, 9, 10, 11
```

La fonction devrait retourner le tableau de tableaux suivant :

```
[[5], [3, 8], [2, 4, 7, 9], [1, 6, 10], [11]]
```

Notez que chaque nombre dans le résultat est en fait un nœud contenant le nombre.
