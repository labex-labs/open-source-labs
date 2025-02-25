# Compress Alt

## Problème

Étant donné une chaîne de caractères, la compresser de telle sorte que les occurrences consécutives du même caractère soient remplacées par ce caractère suivi du nombre d'occurrences. Par exemple, la chaîne 'AAABCCDDDD' deviendrait 'A3BCCD4'. Cependant, si la chaîne compressée n'est pas plus courte que la chaîne d'origine, retourner la chaîne d'origine.

## Exigences

Pour résoudre ce défi, les exigences suivantes doivent être satisfaites :

- La chaîne est supposée être en ASCII.
- La compression est sensible à la casse.
- Des structures de données supplémentaires peuvent être utilisées.
- La chaîne est supposée tenir en mémoire.

## Utilisation de l'exemple

Voici des exemples de manière dont cette fonction peut être utilisée :

- `compress(None)` renvoie `None`
- `compress('')` renvoie `''`
- `compress('AABBCC')` renvoie `'AABBCC'`
- `compress('AAABCCDDDD')` renvoie `'A3BCCD4'`
