# Afficher en binaire

## Problème

Écrire une fonction Python qui prend en entrée un nombre réel compris entre 0 et 1 et renvoie sa représentation binaire sous forme de chaîne de caractères. Si la longueur de la représentation est supérieure à 32, renvoyer 'ERREUR'.

## Exigences

Pour résoudre ce problème, nous devons nous assurer des exigences suivantes :

- L'entrée doit être un flottant.
- La sortie doit être une chaîne de caractères.
- La plage de l'entrée est comprise entre 0 et 1, mais les valeurs 0 et 1 ne sont pas incluses.
- Le résultat doit inclure un zéro final et une virgule décimale.
- Le zéro initial et la virgule décimale sont comptés dans la limite de 32 caractères.
- Nous ne pouvons pas supposer que les entrées sont valides.
- Nous pouvons supposer que le programme s'adapte à la mémoire.

## Utilisation exemple

Voici quelques exemples de comportement attendu de la fonction :

- None -> 'ERREUR'
- Hors limites (0, 1) -> 'ERREUR'
- 0,625 -> 0,101
- 0,987654321 -> 'ERREUR'
