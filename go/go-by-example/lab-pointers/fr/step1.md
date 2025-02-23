# Pointers

Le problème est de comprendre comment les pointeurs fonctionnent en contraste avec les valeurs grâce à deux fonctions : `zeroval` et `zeroptr`. `zeroval` a un paramètre `int`, donc les arguments lui seront passés par valeur. `zeroval` recevra une copie de `ival` distincte de celle de la fonction appelante. En revanche, `zeroptr` a un paramètre `*int`, ce qui signifie qu'il prend un pointeur `int`. Le code `*iptr` dans le corps de la fonction déréférence ensuite le pointeur de son adresse mémoire vers la valeur actuelle à cette adresse. Affecter une valeur à un pointeur déréférencé change la valeur à l'adresse référencée.

- Vous devriez avoir une compréhension de base de Golang.
- Vous devriez savoir comment définir et utiliser des fonctions en Golang.
- Vous devriez savoir comment utiliser des pointeurs en Golang.

```sh
# `zeroval` ne change pas `i` dans `main`, mais
# `zeroptr` le fait car il a une référence à
# l'adresse mémoire de cette variable.
$ go run pointers.go
initial: 1
zeroval: 1
zeroptr: 0
pointer: 0x42131100
```

Voici le code complet ci-dessous :

```go
// Go prend en charge <em><a href="https://en.wikipedia.org/wiki/Pointer_(computer_programming)">les pointeurs</a></em>,
// vous permettant de passer des références à des valeurs et des enregistrements
// dans votre programme.

package main

import "fmt"

// Nous allons montrer comment les pointeurs fonctionnent en contraste avec les valeurs grâce à
// 2 fonctions : `zeroval` et `zeroptr`. `zeroval` a un
// paramètre `int`, donc les arguments lui seront passés par
// valeur. `zeroval` recevra une copie de `ival` distincte
// de celle de la fonction appelante.
func zeroval(ival int) {
	ival = 0
}

// En revanche, `zeroptr` a un paramètre `*int`, ce qui signifie
// qu'il prend un pointeur `int`. Le code `*iptr` dans le
// corps de la fonction déréférence ensuite le pointeur de son
// adresse mémoire vers la valeur actuelle à cette adresse.
// Affecter une valeur à un pointeur déréférencé change la
// valeur à l'adresse référencée.
func zeroptr(iptr *int) {
	*iptr = 0
}

func main() {
	i := 1
	fmt.Println("initial:", i)

	zeroval(i)
	fmt.Println("zeroval:", i)

	// La syntaxe `&i` donne l'adresse mémoire de `i`,
	// c'est-à-dire un pointeur vers `i`.
	zeroptr(&i)
	fmt.Println("zeroptr:", i)

	// Les pointeurs peuvent également être affichés.
	fmt.Println("pointer:", &i)
}

```
