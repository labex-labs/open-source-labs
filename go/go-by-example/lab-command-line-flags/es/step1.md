# Marcas de línea de comandos

Implementa un programa de Golang que analice las marcas de línea de comandos y muestre las opciones analizadas y cualquier argumento posicional restante. El programa debe admitir las siguientes marcas:

- `word`: una marca de tipo string con un valor predeterminado de `"foo"`.
- `numb`: una marca de tipo entero con un valor predeterminado de `42`.
- `fork`: una marca booleana con un valor predeterminado de `false`.
- `svar`: una marca de tipo string que utiliza una variable existente declarada en otro lugar del programa.

- El programa debe utilizar el paquete `flag` para analizar las marcas de línea de comandos.
- El programa debe mostrar las opciones analizadas y cualquier argumento posicional restante.
- El programa debe admitir las marcas `word`, `numb`, `fork` y `svar` como se describe anteriormente.

```sh
# Para experimentar con el programa de marcas de línea de comandos, es
# mejor compilarlo primero y luego ejecutar el binario resultante
# directamente.
$ go build command-line-flags.go

# Prueba el programa compilado dando primero valores para
# todas las marcas.
$./command-line-flags -word=opt -numb=7 -fork -svar=flag
word: opt
numb: 7
fork: true
svar: flag
tail: []

# Tenga en cuenta que si omite una marca, automáticamente toma
# sus valores predeterminados.
$./command-line-flags -word=opt
word: opt
numb: 42
fork: false
svar: bar
tail: []

# Se pueden proporcionar argumentos posicionales restantes después
# de cualquier marca.
$./command-line-flags -word=opt a1 a2 a3
word: opt
...
tail: [a1 a2 a3]

# Tenga en cuenta que el paquete `flag` requiere que todas las
# marcas aparezcan antes de los argumentos posicionales (de lo
# contrario, las marcas se interpretarán como argumentos
# posicionales).
$./command-line-flags -word=opt a1 a2 a3 -numb=7
word: opt
numb: 42
fork: false
svar: bar
tail: [a1 a2 a3 -numb=7]

# Utilice las marcas `-h` o `--help` para obtener el texto de ayuda
# automáticamente generado para el programa de línea de comandos.
$./command-line-flags -h
Uso de./command-line-flags:
-fork=false: un bool
-numb=42: un int
-svar="bar": una variable string
-word="foo": una string

# Si proporciona una marca que no se especificó en el
# paquete `flag`, el programa imprimirá un mensaje de error
# y mostrará nuevamente el texto de ayuda.
$./command-line-flags -wat
flag proporcionada pero no definida: -wat
Uso de./command-line-flags:
...
```

A continuación está el código completo:

```go
// [_Marcas de línea de comandos_](https://en.wikipedia.org/wiki/Command-line_interface#Command-line_option)
// son una forma común de especificar opciones para los programas
// de línea de comandos. Por ejemplo, en `wc -l` el `-l` es una
// marca de línea de comandos.

package main

// Go proporciona un paquete `flag` que admite el análisis básico
// de las marcas de línea de comandos. Utilizaremos este paquete
// para implementar nuestro programa de ejemplo de línea de comandos.
import (
	"flag"
	"fmt"
)

func main() {

	// Las declaraciones básicas de marcas están disponibles para
	// opciones de tipo string, entero y booleano. Aquí declaramos
	// una marca de string `word` con un valor predeterminado
	// `"foo"` y una descripción breve. Esta función `flag.String`
	// devuelve un puntero de string (no un valor de string);
	// veremos cómo utilizar este puntero más adelante.
	wordPtr := flag.String("word", "foo", "una string")

	// Esto declara las marcas `numb` y `fork`, utilizando un
	// enfoque similar a la marca `word`.
	numbPtr := flag.Int("numb", 42, "un int")
	forkPtr := flag.Bool("fork", false, "un bool")

	// También es posible declarar una opción que utiliza una
	// variable existente declarada en otro lugar del programa.
	// Tenga en cuenta que debemos pasar un puntero a la función
	// de declaración de la marca.
	var svar string
	flag.StringVar(&svar, "svar", "bar", "una variable string")

	// Una vez declaradas todas las marcas, llame a `flag.Parse()`
	// para ejecutar el análisis de la línea de comandos.
	flag.Parse()

	// Aquí simplemente mostraremos las opciones analizadas y
	// cualquier argumento posicional restante. Tenga en cuenta
	// que debemos desreferenciar los punteros con, por ejemplo,
	// `*wordPtr` para obtener los valores reales de las opciones.
	fmt.Println("word:", *wordPtr)
	fmt.Println("numb:", *numbPtr)
	fmt.Println("fork:", *forkPtr)
	fmt.Println("svar:", svar)
	fmt.Println("tail:", flag.Args())
}

```
