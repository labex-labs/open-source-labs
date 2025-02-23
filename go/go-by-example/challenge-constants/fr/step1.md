# Constante

Le problème à résoudre est de démontrer l'utilisation des constantes en Golang pour les valeurs de caractères, de chaînes, de booléens et de numériques.

## Exigences

Le défi a les exigences suivantes :

- Utiliser le mot clé `const` pour déclarer une valeur constante.
- Les constantes doivent être de valeurs de caractères, de chaînes, de booléens et de numériques.
- Une instruction constante peut apparaître n'importe où qu'une instruction `var` peut l'être.
- Démontrez que les expressions constantes effectuent des calculs avec une précision arbitraire.
- Une constante numérique n'a pas de type tant qu'elle n'en est pas donnée un, par exemple par une conversion explicite.
- Un nombre peut être donné un type en l'utilisant dans un contexte qui en exige un, tel qu'une affectation de variable ou un appel de fonction.

## Exemple

```sh
$ go run constant.go
constant
6e+11
600000000000
-0.28470407323754404
```
