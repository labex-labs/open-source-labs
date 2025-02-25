# Permutation

## Problème

Étant donné deux chaînes de caractères, nous devons déterminer si l'une est une permutation de l'autre. Une permutation est définie comme un réarrangement des caractères dans une chaîne. Par exemple, "act" est une permutation de "cat".

## Exigences

Pour résoudre ce problème, nous devons prendre en compte les exigences suivantes :

- La chaîne est en ASCII.
- Les espaces blancs sont importants.
- La comparaison est sensible à la casse. Par exemple, "Nib" et "bin" ne correspondent pas.
- Nous pouvons utiliser des structures de données supplémentaires.
- Nous pouvons supposer que les chaînes entrent en mémoire.

## Utilisation de l'exemple

Voici quelques exemples d'utilisation de cette fonction :

- Un ou plusieurs entrées None -> Faux
- Une ou plusieurs chaînes vides -> Faux
- 'Nib', 'bin' -> Faux
- 'act', 'cat' -> Vrai
- 'a ct', 'ca t' -> Vrai
