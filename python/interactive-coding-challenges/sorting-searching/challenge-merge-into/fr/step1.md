# Fusionner dans

## Problème

Étant donné deux tableaux triés A et B, fusionnez B dans A dans l'ordre trié. Les tableaux peuvent contenir des éléments dupliqués, et les entrées peuvent ne pas être valides. Les entrées incluront également la taille réelle de A et B, et on peut supposer que cela tient en mémoire.

Pour résoudre ce problème, nous devons considérer si A a assez d'espace pour B, et si les entrées ont des éléments dupliqués dans le tableau. Si A n'a pas assez d'espace pour B, nous devons peut-être allouer de la mémoire supplémentaire. Si les entrées ont des éléments dupliqués dans le tableau, nous devons nous assurer que ces doublons sont gérés correctement lors de la fusion.

## Exigences

Pour résoudre ce problème, nous devons répondre aux exigences suivantes :

- Vérifier que A a assez d'espace pour B
- Gérer correctement les éléments dupliqués dans le tableau
- Vérifier que les entrées sont valides
- Inclure la taille réelle de A et B dans les entrées
- Supposer que les entrées tiennent en mémoire

## Utilisation de l'exemple

Pour illustrer comment ce problème peut être résolu, considérez les exemples suivants :

- Si A ou B est None, une exception doit être levée.
- Si l'index du dernier élément de A ou B est inférieur à 0, une exception doit être levée.
- Si A ou B est vide, le résultat doit être A ou B respectivement.
- Dans le cas général, nous pouvons fusionner B dans A comme suit :

```
A = [1, 3, 5, 7, 9, None, None, None]
B = [4, 5, 6]
A = [1, 3, 4, 5, 5, 6, 7, 9]
```
