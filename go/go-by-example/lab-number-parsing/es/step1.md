# Análisis de números

El análisis de números a partir de cadenas es una tarea común en muchos programas. En este laboratorio se te pide que uses el paquete integrado `strconv` para analizar diferentes tipos de números a partir de cadenas.

- Utiliza el paquete `strconv` para analizar números a partir de cadenas.
- Analiza un número de punto flotante con `ParseFloat`.
- Analiza un entero con `ParseInt`.
- Analiza un número con formato hexadecimal con `ParseInt`.
- Analiza un entero sin signo con `ParseUint`.
- Analiza un entero en base 10 con `Atoi`.
- Maneja los errores devueltos por las funciones de análisis.

```sh
$ go run number-parsing.go
1.234
123
456
789
135
strconv.ParseInt: parsing "wat": invalid syntax

# A continuación, veremos otra tarea de análisis común: URLs.
```

A continuación está el código completo:

```go
// El análisis de números a partir de cadenas es una tarea básica pero común
// en muchos programas; aquí está cómo hacerlo en Go.

package main

// El paquete integrado `strconv` proporciona el análisis de números.
import (
	"fmt"
	"strconv"
)

func main() {

	// Con `ParseFloat`, este `64` indica cuántos bits de precisión se deben analizar.
	f, _ := strconv.ParseFloat("1.234", 64)
	fmt.Println(f)

	// Para `ParseInt`, el `0` significa inferir la base a partir de la cadena. `64` requiere que el resultado quepa en 64 bits.
	i, _ := strconv.ParseInt("123", 0, 64)
	fmt.Println(i)

	// `ParseInt` reconocerá números con formato hexadecimal.
	d, _ := strconv.ParseInt("0x1c8", 0, 64)
	fmt.Println(d)

	// También está disponible `ParseUint`.
	u, _ := strconv.ParseUint("789", 0, 64)
	fmt.Println(u)

	// `Atoi` es una función de conveniencia para el análisis básico de enteros en base 10.
	k, _ := strconv.Atoi("135")
	fmt.Println(k)

	// Las funciones de análisis devuelven un error en caso de entrada incorrecta.
	_, e := strconv.Atoi("wat")
	fmt.Println(e)
}

```
