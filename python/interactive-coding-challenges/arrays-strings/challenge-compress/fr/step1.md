# Compress

## Problème

Étant donné une chaîne de caractères, la compresser de telle sorte que 'AAABCCDDDD' devienne 'A3BC2D4'. La chaîne compressée ne doit être retournée que si elle économise de l'espace. Si la chaîne compressée est plus longue que la chaîne d'origine, retourner la chaîne d'origine. La chaîne est sensible à la casse et peut être supposée être en ASCII. Des structures de données supplémentaires peuvent être utilisées et on peut supposer que la chaîne tient en mémoire.

## Exigences

Les exigences suivantes doivent être satisfaites :

- La chaîne est en ASCII.
- La chaîne est sensible à la casse.
- Des structures de données supplémentaires peuvent être utilisées.
- La chaîne tient en mémoire.

## Utilisation de l'exemple

Les exemples suivants démontrent l'entrée et la sortie attendues de la fonction :

- None -> None
- '' -> ''
- 'AABBCC' -> 'AABBCC'
- 'AAABCCDDDD' -> 'A3BC2D4'
