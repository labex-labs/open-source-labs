# Switch

Dans ce laboratoire, vous devez compléter l'instruction `switch` pour afficher le message correspondant en fonction de la valeur d'entrée.

- L'instruction `switch` doit être utilisée pour résoudre le problème.
- Le cas `default` doit être utilisé pour gérer les valeurs d'entrée inattendues.

```sh
$ go run switch.go
Écrivez 2 sous forme de deux
C'est un jour de semaine
C'est après midi
Je suis un booléen
Je suis un entier
Je ne connais pas le type string
```

Voici le code complet ci-dessous :

```go
// Les instructions `switch` expriment des conditionnels sur de nombreux
// branches.

package main

import (
	"fmt"
	"time"
)

func main() {

	// Voici un `switch` de base.
	i := 2
	fmt.Print("Écrivez ", i, " sous forme de ")
	switch i {
	case 1:
		fmt.Println("un")
	case 2:
		fmt.Println("deux")
	case 3:
		fmt.Println("trois")
	}

	// Vous pouvez utiliser des virgules pour séparer plusieurs expressions
	// dans la même instruction `case`. Nous utilisons également le cas
	// `default` optionnel dans cet exemple.
	switch time.Now().Weekday() {
	case time.Saturday, time.Sunday:
		fmt.Println("C'est le week-end")
	default:
		fmt.Println("C'est un jour de semaine")
	}

	// Un `switch` sans expression est une autre manière
	// d'exprimer la logique if/else. Ici, nous montrons également comment
	// les expressions `case` peuvent être non constantes.
	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("C'est avant midi")
	default:
		fmt.Println("C'est après midi")
	}

	// Un `switch` de type compare les types au lieu des valeurs. Vous
	// pouvez utiliser cela pour découvrir le type d'une valeur d'interface.
	// Dans cet exemple, la variable `t` aura le type correspondant à sa clause.
	whatAmI := func(i interface{}) {
		switch t := i.(type) {
		case bool:
			fmt.Println("Je suis un booléen")
		case int:
			fmt.Println("Je suis un entier")
		default:
			fmt.Printf("Je ne connais pas le type %T\n", t)
		}
	}
	whatAmI(true)
	whatAmI(1)
	whatAmI("hey")
}

```
