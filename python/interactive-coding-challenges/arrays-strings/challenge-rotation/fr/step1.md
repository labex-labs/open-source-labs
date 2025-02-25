# Rotation

## Problème

Étant donné deux chaînes s1 et s2, déterminer si s1 est une rotation de s2 en appelant (une seule fois) une fonction is_substring. La fonction is_substring prend deux chaînes en entrée et renvoie True si la première chaîne est une sous-chaîne de la seconde chaîne, et False sinon.

## Exigences

Pour résoudre ce problème, nous devons répondre aux exigences suivantes :

- La chaîne est en ASCII.
- La comparaison est sensible à la casse.
- Nous pouvons utiliser des structures de données supplémentaires.
- Les chaînes peuvent tenir en mémoire.

## Utilisation d'exemple

Voici quelques exemples de comportement attendu de la fonction :

- Si les chaînes ont des tailles différentes, la fonction devrait renvoyer False.
- Si l'une des chaînes est None, la fonction devrait renvoyer False.
- Si l'une des chaînes est un espace et l'autre pas, la fonction devrait renvoyer False.
- Si les deux chaînes sont des espaces, la fonction devrait renvoyer True.
- Si s1 est une rotation de s2, la fonction devrait renvoyer True.
