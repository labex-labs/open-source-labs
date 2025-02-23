# Pointers

Le problème est de comprendre comment les pointeurs fonctionnent en contraste avec les valeurs grâce à deux fonctions : `zeroval` et `zeroptr`. `zeroval` a un paramètre `int`, donc les arguments lui seront passés par valeur. `zeroval` recevra une copie de `ival` distincte de celle de la fonction appelante. En revanche, `zeroptr` a un paramètre `*int`, ce qui signifie qu'il prend un pointeur `int`. Le code `*iptr` dans le corps de la fonction déréférence ensuite le pointeur de son adresse mémoire vers la valeur actuelle à cette adresse. Affecter une valeur à un pointeur déréférencé change la valeur à l'adresse référencée.

## Exigences

- Vous devriez avoir une compréhension de base de Golang.
- Vous devriez savoir comment définir et utiliser des fonctions en Golang.
- Vous devriez savoir comment utiliser des pointeurs en Golang.

## Exemple

```sh
# `zeroval` ne modifie pas `i` dans `main`, mais
# `zeroptr` le fait car il a une référence à
# l'adresse mémoire de cette variable.
$ go run pointers.go
initial: 1
zeroval: 1
zeroptr: 0
pointer: 0x42131100
```
