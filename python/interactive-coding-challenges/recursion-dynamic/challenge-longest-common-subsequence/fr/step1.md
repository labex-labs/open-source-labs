# Plus longue sous-suite commune

## Problème

Étant donné deux chaînes de caractères, trouver la plus longue sous-suite commune. Une sous-suite est une séquence qui peut être dérivée d'une autre séquence en supprimant certains éléments ou aucun élément sans changer l'ordre des éléments restants. Par exemple, "ACE" est une sous-suite de "ABCDE" mais pas de "AEDCA".

## Exigences

Pour résoudre ce problème, les exigences suivantes doivent être satisfaites :

- Les entrées peuvent ne pas être valides, donc le programme devrait gérer les entrées invalides.
- Les chaînes de caractères sont en ASCII.
- Le programme devrait être sensible à la casse.
- Une sous-suite est un bloc non contigu de caractères.
- Le programme devrait renvoyer une chaîne de caractères en tant que résultat.
- Le programme devrait supposer qu'il s'adapte à la mémoire.

## Utilisation exemple

Voici quelques exemples de comportement attendu du programme :

- Si str0 ou str1 est None, une exception devrait être levée.
- Si str0 ou str1 est égal à 0, une chaîne de caractères vide devrait être renvoyée.
- Cas général :

```
str0 = 'ABCDEFGHIJ'
str1 = 'FOOBCDBCDE'

résultat : 'BCDE'
```
