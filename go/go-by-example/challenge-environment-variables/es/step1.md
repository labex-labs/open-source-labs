# Variables de entorno

En este desafío, deberás establecer, obtener y listar variables de entorno.

## Requisitos

- Utiliza `os.Setenv` para establecer un par clave/valor.
- Utiliza `os.Getenv` para obtener un valor para una clave.
- Utiliza `os.Environ` para listar todos los pares clave/valor en el entorno.
- Utiliza `strings.SplitN` para dividir la clave y el valor.

## Ejemplo

```sh
# Al ejecutar el programa se muestra que recogemos el valor
# de `FOO` que establecemos en el programa, pero que
# `BAR` está vacío.
$ go run environment-variables.go
FOO: 1
BAR:

# La lista de claves en el entorno dependerá de tu
# máquina en particular.
TERM_PROGRAM
PATH
SHELL
...
FOO

# Si establecemos `BAR` en el entorno primero, el programa
# en ejecución recoge ese valor.
$ BAR=2 go run environment-variables.go
FOO: 1
BAR: 2
...
```
