# Diff de chaînes de caractères

## Problème

Étant données deux chaînes de caractères, nous devons trouver le seul caractère différent entre elles. Les chaînes de caractères sont supposées être en ASCII et en minuscules. Nous ne pouvons pas supposer que les entrées sont valides, donc nous devons vérifier si elles sont nulles. Si les entrées sont valides, nous pouvons supposer qu'il n'y a qu'un seul caractère différent entre les deux chaînes de caractères. Nous devons également nous assurer que la solution tient en mémoire.

## Exigences

Pour résoudre ce problème, nous devons prendre en compte les exigences suivantes :

- Les chaînes de caractères sont en ASCII.
- Les chaînes de caractères sont en minuscules.
- Nous devons vérifier si l'entrée est nulle.
- Il n'y a qu'un seul caractère différent entre les deux chaînes de caractères.
- La solution devrait tenir en mémoire.

## Utilisation de l'exemple

Voici quelques exemples d'utilisation de la fonction :

- Entrée nulle -> TypeError
- 'ab', 'aab' -> 'a'
- 'aab', 'ab' -> 'a'
- 'abcd', 'abcde' -> 'e'
- 'aaabbcdd', 'abdbacade' -> 'e'
