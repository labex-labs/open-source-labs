# Ajouter les chiffres

## Problème

Étant donné un entier, nous devons additionner ses chiffres de manière répétée jusqu'à ce que le résultat soit un seul chiffre. Par exemple, si nous sommes donnés l'entier 138, nous additionnons 1 + 3 + 8 = 12. Puisque 12 n'est pas un seul chiffre, nous répétons le processus et additionnons 1 + 2 = 3. Par conséquent, le résultat final est 3.

## Exigences

Pour résoudre ce problème, nous devons prendre en compte les exigences suivantes :

- L'entier d'entrée n'est pas négatif.
- Les entrées ne sont pas toujours valides, donc nous devons gérer tout éventuel erreur qui pourrait survenir.
- La solution doit tenir dans la mémoire.

## Utilisation de l'exemple

Voici quelques exemples de manière dont cette fonction peut être utilisée :

- Si nous passons None en tant qu'entrée, la fonction doit lever une TypeError.
- Si nous passons un entier négatif en tant qu'entrée, la fonction doit lever une ValueError.
- Si nous passons 9 en tant qu'entrée, la fonction doit renvoyer 9 puisque c'est déjà un seul chiffre.
- Si nous passons 138 en tant qu'entrée, la fonction doit renvoyer 3.
- Si nous passons 65536 en tant qu'entrée, la fonction doit renvoyer 7.
