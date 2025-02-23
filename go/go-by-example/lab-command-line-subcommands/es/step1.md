# Subcomandos de línea de comandos

Se te pide crear un programa que soporte dos subcomandos, `foo` y `bar`, cada uno con su propio conjunto de flags. El subcomando `foo` debe tener dos flags, `enable` y `name`, mientras que el subcomando `bar` debe tener un flag, `level`.

- El programa debe usar el paquete `flag` para definir y analizar los flags.
- El subcomando `foo` debe tener dos flags, `enable` y `name`, ambos de tipo string.
- El subcomando `bar` debe tener un flag, `level`, de tipo int.
- El programa debe imprimir un mensaje de error si se proporciona un subcomando no válido.
- El programa debe imprimir los valores de los flags para el subcomando que se invoca.

```sh
$ go build command-line-subcommands.go

# Primero invoca el subcomando foo.
$./command-line-subcommands foo -enable -name=joe a1 a2
subcommand 'foo'
enable: true
name: joe
tail: [a1 a2]

# Ahora prueba bar.
$./command-line-subcommands bar -level 8 a1
subcommand 'bar'
level: 8
tail: [a1]

# Pero bar no aceptará los flags de foo.
$./command-line-subcommands bar -enable a1
flag provided but not defined: -enable
Usage of bar:
-level int
level

# A continuación veremos las variables de entorno, otra forma
# común de parametrizar los programas.
```

A continuación se muestra el código completo:

```go
// Algunas herramientas de línea de comandos, como la herramienta `go` o `git`
// tienen muchos *subcomandos*, cada uno con su propio conjunto de
// flags. Por ejemplo, `go build` y `go get` son dos
// subcomandos diferentes de la herramienta `go`.
// El paquete `flag` nos permite definir fácilmente subcomandos simples
// que tienen sus propios flags.

package main

import (
	"flag"
	"fmt"
	"os"
)

func main() {

	// Declaramos un subcomando usando la función `NewFlagSet`
	// y procedemos a definir nuevos flags específicos
	// para este subcomando.
	fooCmd := flag.NewFlagSet("foo", flag.ExitOnError)
	fooEnable := fooCmd.Bool("enable", false, "enable")
	fooName := fooCmd.String("name", "", "name")

	// Para un subcomando diferente podemos definir diferentes
	// flags admitidos.
	barCmd := flag.NewFlagSet("bar", flag.ExitOnError)
	barLevel := barCmd.Int("level", 0, "level")

	// El subcomando se espera como primer argumento
	// del programa.
	if len(os.Args) < 2 {
		fmt.Println("expected 'foo' or 'bar' subcommands")
		os.Exit(1)
	}

	// Comprobamos qué subcomando se invoca.
	switch os.Args[1] {

	// Para cada subcomando, analizamos sus propios flags y
	// tenemos acceso a los argumentos posicionales finales.
	case "foo":
		fooCmd.Parse(os.Args[2:])
		fmt.Println("subcommand 'foo'")
		fmt.Println("  enable:", *fooEnable)
		fmt.Println("  name:", *fooName)
		fmt.Println("  tail:", fooCmd.Args())
	case "bar":
		barCmd.Parse(os.Args[2:])
		fmt.Println("subcommand 'bar'")
		fmt.Println("  level:", *barLevel)
		fmt.Println("  tail:", barCmd.Args())
	default:
		fmt.Println("expected 'foo' or 'bar' subcommands")
		os.Exit(1)
	}
}

```
