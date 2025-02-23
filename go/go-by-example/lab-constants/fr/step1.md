# Constantes

Le problème à résoudre est de démontrer l'utilisation des constantes en Golang pour les valeurs de caractères, de chaînes de caractères, de booléens et de numériques.

Le laboratoire a les exigences suivantes :

- Utiliser le mot-clé `const` pour déclarer une valeur constante.
- Les constantes doivent être de type caractère, chaîne de caractères, booléen et numérique.
- Une déclaration de constante peut apparaître n'importe où qu'une déclaration `var` peut apparaître.
- Démontrez que les expressions constantes effectuent des calculs avec une précision arbitraire.
- Une constante numérique n'a pas de type tant qu'elle n'en a pas été donnée, par exemple par une conversion explicite.
- Un nombre peut être donné un type en l'utilisant dans un contexte qui en exige un, tel qu'une affectation de variable ou un appel de fonction.

```sh
$ go run constant.go
constant
6e+11
600000000000
-0.28470407323754404
```

Voici le code complet ci-dessous :

```go
// Go prend en charge les _constantes_ de type caractère, chaîne de caractères, booléen,
// et valeurs numériques.

package main

import (
	"fmt"
	"math"
)

// `const` déclare une valeur constante.
const s string = "constant"

func main() {
	fmt.Println(s)

	// Une déclaration `const` peut apparaître n'importe où qu'une déclaration `var`
	// peut apparaître.
	const n = 500000000

	// Les expressions constantes effectuent des calculs avec
	// une précision arbitraire.
	const d = 3e20 / n
	fmt.Println(d)

	// Une constante numérique n'a pas de type tant qu'elle n'en a pas été donnée
	// une, par exemple par une conversion explicite.
	fmt.Println(int64(d))

	// Un nombre peut être donné un type en l'utilisant dans un
	// contexte qui en exige un, tel qu'une affectation de variable
	// ou un appel de fonction. Par exemple, ici
	// `math.Sin` attend un `float64`.
	fmt.Println(math.Sin(n))
}

```
