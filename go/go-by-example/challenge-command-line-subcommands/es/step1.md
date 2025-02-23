# Subcomandos de línea de comandos

Se te pide crear un programa que soporte dos subcomandos, `foo` y `bar`, cada uno con su propio conjunto de flags. El subcomando `foo` debe tener dos flags, `enable` y `name`, mientras que el subcomando `bar` debe tener un flag, `level`.

## Requisitos

- El programa debe usar el paquete `flag` para definir y analizar los flags.
- El subcomando `foo` debe tener dos flags, `enable` y `name`, ambos de tipo string.
- El subcomando `bar` debe tener un flag, `level`, de tipo int.
- El programa debe imprimir un mensaje de error si se proporciona un subcomando no válido.
- El programa debe imprimir los valores de los flags para el subcomando que se invoca.

## Ejemplo

```sh
$ go build command-line-subcommands.go

# Primero invoca el subcomando foo.
$./command-line-subcommands foo -enable -name=joe a1 a2
subcomando 'foo'
enable: true
name: joe
tail: [a1 a2]

# Ahora prueba bar.
$./command-line-subcommands bar -level 8 a1
subcomando 'bar'
level: 8
tail: [a1]

# Pero bar no aceptará los flags de foo.
$./command-line-subcommands bar -enable a1
flag provided but not defined: -enable
Usage of bar:
-level int
level

# A continuación veremos las variables de entorno, otra forma común
# de parametrizar los programas.
```
