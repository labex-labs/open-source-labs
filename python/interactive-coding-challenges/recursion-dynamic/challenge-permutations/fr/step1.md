# Permutations

## Problème

Étant donné une chaîne de caractères d'entrée, la tâche consiste à trouver toutes les permutations possibles des caractères de la chaîne. La sortie devrait être une liste de chaînes de caractères, où chaque chaîne représente une permutation unique de la chaîne d'entrée. La chaîne d'entrée peut contenir des doublons, mais la sortie ne devrait pas en avoir.

## Exigences

Pour résoudre ce problème, nous devons prendre en compte les exigences suivantes :

- L'entrée peut contenir des doublons.
- La sortie ne devrait pas avoir de doublons.
- La sortie devrait être une liste de chaînes de caractères.
- Les résultats n'ont pas besoin d'être triés.
- Les entrées ne sont pas toujours valides.
- La solution devrait tenir en mémoire.

## Utilisation de l'exemple

Voici quelques exemples de comment la fonction devrait se comporter :

- Si l'entrée est None, la sortie devrait être None.
- Si l'entrée est une chaîne de caractères vide, la sortie devrait être une chaîne de caractères vide.
- Si l'entrée est 'AABC', la sortie devrait être ['AABC', 'AACB', 'ABAC', 'ABCA', 'ACAB', 'ACBA', 'BAAC', 'BACA', 'BCAA', 'CAAB', 'CABA', 'CBAA'].
