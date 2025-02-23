# Analyse de nombres

L'analyse de nombres à partir de chaînes de caractères est une tâche courante dans de nombreux programmes. Ce laboratoire vous demande d'utiliser le package intégré `strconv` pour analyser différents types de nombres à partir de chaînes de caractères.

- Utilisez le package `strconv` pour analyser des nombres à partir de chaînes de caractères.
- Analysez un nombre à virgule flottante avec `ParseFloat`.
- Analysez un entier avec `ParseInt`.
- Analysez un nombre au format hexadécimal avec `ParseInt`.
- Analysez un entier non signé avec `ParseUint`.
- Analysez un entier en base 10 avec `Atoi`.
- Gérez les erreurs renvoyées par les fonctions d'analyse.

```sh
$ go run number-parsing.go
1.234
123
456
789
135
strconv.ParseInt: parsing "wat": invalid syntax

# Ensuite, nous examinerons une autre tâche d'analyse courante : les URL.
```

Voici le code complet ci-dessous :

```go
// L'analyse de nombres à partir de chaînes de caractères est une tâche
// de base mais courante dans de nombreux programmes ; voici comment
// le faire en Go.

package main

// Le package intégré `strconv` fournit l'analyse
// des nombres.
import (
	"fmt"
	"strconv"
)

func main() {

	// Avec `ParseFloat`, ce `64` indique combien de bits
	// de précision analyser.
	f, _ := strconv.ParseFloat("1.234", 64)
	fmt.Println(f)

	// Pour `ParseInt`, le `0` signifie déduire la base à
	// partir de la chaîne. `64` exige que le résultat
	// rentre dans 64 bits.
	i, _ := strconv.ParseInt("123", 0, 64)
	fmt.Println(i)

	// `ParseInt` reconnaîtra les nombres au format hexadécimal.
	d, _ := strconv.ParseInt("0x1c8", 0, 64)
	fmt.Println(d)

	// Un `ParseUint` est également disponible.
	u, _ := strconv.ParseUint("789", 0, 64)
	fmt.Println(u)

	// `Atoi` est une fonction pratique pour l'analyse
	// de base-10 des `int`.
	k, _ := strconv.Atoi("135")
	fmt.Println(k)

	// Les fonctions d'analyse renvoient une erreur en cas
	// d'entrée incorrecte.
	_, e := strconv.Atoi("wat")
	fmt.Println(e)
}

```
