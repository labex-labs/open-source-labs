# Plus longue sous-chaîne

## Problème

Étant données deux chaînes de caractères, la tâche consiste à trouver la plus longue sous-chaîne commune. Une sous-chaîne est un bloc contigu de caractères. La solution doit être sensible à la casse et supposer que les chaînes sont en ASCII. La sortie devrait être une chaîne de caractères et le programme devrait supposer que les entrées ne sont pas nécessairement valides. Cependant, il peut supposer que le problème tient en mémoire.

## Exigences

Pour résoudre ce problème, le programme doit répondre aux exigences suivantes :

- Les entrées ne sont pas nécessairement valides.
- Les chaînes sont en ASCII.
- La solution doit être sensible à la casse.
- Une sous-chaîne est un bloc contigu de caractères.
- La sortie devrait être une chaîne de caractères.
- Le programme devrait supposer que le problème tient en mémoire.

## Utilisation de l'exemple

Le programme devrait se comporter comme suit :

- Si str0 ou str1 est None, une exception devrait être levée.
- Si str0 ou str1 est égal à 0, la sortie devrait être une chaîne de caractères vide.
- En général, étant donné str0 = 'ABCDEFGHIJ' et str1 = 'FOOBCDBCDE', la sortie devrait être 'BCDE'.
