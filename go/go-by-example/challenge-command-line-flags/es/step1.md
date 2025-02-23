# Banderas de línea de comandos

Implementa un programa de Golang que analice las banderas de línea de comandos y muestre las opciones analizadas y cualquier argumento posicional final. El programa debe admitir las siguientes banderas:

- `word`: una bandera de tipo string con un valor predeterminado de `"foo"`.
- `numb`: una bandera de tipo entero con un valor predeterminado de `42`.
- `fork`: una bandera booleana con un valor predeterminado de `false`.
- `svar`: una bandera de tipo string que utiliza una variable existente declarada en otro lugar del programa.

## Requisitos

- El programa debe utilizar el paquete `flag` para analizar las banderas de línea de comandos.
- El programa debe mostrar las opciones analizadas y cualquier argumento posicional final.
- El programa debe admitir las banderas `word`, `numb`, `fork` y `svar` como se describe anteriormente.

## Ejemplo

```sh
# Para experimentar con el programa de banderas de línea de comandos,
# es mejor compilarlo primero y luego ejecutar el binario resultante
# directamente.
$ go build command-line-flags.go

# Prueba el programa compilado proporcionándole valores
# para todas las banderas primero.
$./command-line-flags -word=opt -numb=7 -fork -svar=flag
word: opt
numb: 7
fork: true
svar: flag
tail: []

# Tenga en cuenta que si omite las banderas, estas toman
# automáticamente sus valores predeterminados.
$./command-line-flags -word=opt
word: opt
numb: 42
fork: false
svar: bar
tail: []

# Los argumentos posicionales finales se pueden proporcionar después
# de cualquier bandera.
$./command-line-flags -word=opt a1 a2 a3
word: opt
...
tail: [a1 a2 a3]

# Tenga en cuenta que el paquete `flag` requiere que todas las banderas
# aparezcan antes de los argumentos posicionales (de lo contrario, las
# banderas se interpretarán como argumentos posicionales).
$./command-line-flags -word=opt a1 a2 a3 -numb=7
word: opt
numb: 42
fork: false
svar: bar
tail: [a1 a2 a3 -numb=7]

# Utilice las banderas `-h` o `--help` para obtener el texto de ayuda
# automáticamente generado para el programa de línea de comandos.
$./command-line-flags -h
Usage of./command-line-flags:
-fork=false: a bool
-numb=42: an int
-svar="bar": a string var
-word="foo": a string

# Si proporciona una bandera que no se especificó en el
# paquete `flag`, el programa imprimirá un mensaje de error
# y mostrará nuevamente el texto de ayuda.
$./command-line-flags -wat
flag provided but not defined: -wat
Usage of./command-line-flags:
...
```
