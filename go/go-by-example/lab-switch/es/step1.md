# Switch

En este laboratorio, debes completar la instrucción `switch` para imprimir el mensaje correspondiente según el valor de entrada.

- La instrucción `switch` debe utilizarse para resolver el problema.
- El caso `default` debe utilizarse para manejar valores de entrada inesperados.

```sh
$ go run switch.go
Escribe 2 como two
Es un día laboral
Es después del mediodía
Soy un bool
Soy un int
No sé el tipo string
```

A continuación se muestra el código completo:

```go
// Las instrucciones `switch` expresan condicionales en muchas
// ramas.

package main

import (
	"fmt"
	"time"
)

func main() {

	// Aquí hay un `switch` básico.
	i := 2
	fmt.Print("Escribe ", i, " como ")
	switch i {
	case 1:
		fmt.Println("uno")
	case 2:
		fmt.Println("dos")
	case 3:
		fmt.Println("tres")
	}

	// Puedes usar comas para separar múltiples expresiones
	// en la misma instrucción `case`. También usamos el caso
	// `default` opcional en este ejemplo.
	switch time.Now().Weekday() {
	case time.Saturday, time.Sunday:
		fmt.Println("Es el fin de semana")
	default:
		fmt.Println("Es un día laboral")
	}

	// `switch` sin una expresión es una forma alternativa
	// de expresar la lógica if/else. Aquí también mostramos cómo
	// las expresiones `case` pueden no ser constantes.
	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("Es antes del mediodía")
	default:
		fmt.Println("Es después del mediodía")
	}

	// Un `switch` de tipo compara tipos en lugar de valores. Puedes
	// usar esto para descubrir el tipo de un valor de interfaz.
	// En este ejemplo, la variable `t` tendrá el tipo
	// correspondiente a su cláusula.
	whatAmI := func(i interface{}) {
		switch t := i.(type) {
		case bool:
			fmt.Println("Soy un bool")
		case int:
			fmt.Println("Soy un int")
		default:
			fmt.Printf("No sé el tipo %T\n", t)
		}
	}
	whatAmI(true)
	whatAmI(1)
	whatAmI("hey")
}

```
