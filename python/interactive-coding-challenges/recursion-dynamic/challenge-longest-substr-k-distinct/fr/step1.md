# Plus longue sous-chaîne avec k caractères distincts

## Problème

Étant donné une chaîne de caractères et un entier k, trouver la longueur de la plus longue sous-chaîne qui contient au plus k caractères distincts. Une sous-chaîne est un bloc contigu de caractères. Par exemple, dans la chaîne "abcabcdefgghiij", la plus longue sous-chaîne avec au plus 3 caractères distincts est "abcabc". Si plusieurs sous-chaînes ont la même longueur, renvoyer n'importe laquelle d'entre elles.

## Exigences

Pour résoudre ce défi, les exigences suivantes doivent être satisfaites :

- Les entrées peuvent ne pas être valides, donc le code devrait gérer les entrées invalides de manière appropriée.
- Les chaînes de caractères sont en ASCII.
- La recherche est sensible à la casse.
- Une sous-chaîne est un bloc contigu de caractères.
- Le résultat devrait être un entier.
- Le code devrait être capable de gérer l'entrée dans les limites de la mémoire.

## Utilisation de l'exemple

Les exemples suivants démontrent le comportement attendu du code :

- Aucune -> TypeError
- '', k = 3 -> 0
- 'abcabcdefgghiij', k=3 -> 6
- 'abcabcdefgghighij', k=3 -> 7
