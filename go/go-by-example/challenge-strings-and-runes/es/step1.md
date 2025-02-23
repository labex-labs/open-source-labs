# Cadenas y runas

El problema que se debe resolver en este desafío es entender cómo trabajar con cadenas y runas en Go. En particular, el desafío cubrirá cómo obtener la longitud de una cadena, cómo acceder a un índice de una cadena, cómo contar el número de runas en una cadena y cómo iterar sobre las runas en una cadena.

## Requisitos

Para completar este desafío, se necesitará:

- Un conocimiento básico de la sintaxis de Go
- Conocimiento de las cadenas y runas de Go
- La biblioteca estándar de Go

## Ejemplo

```sh
$ go run strings-and-runes.go
Longitud: 18
e0 b8 aa e0 b8 a7 e0 b8 b1 e0 b8 aa e0 b8 94 e0 b8 b5
Número de runas: 6
U+0E2A 'ส' comienza en 0
U+0E27 'ว' comienza en 3
U+0E31 'ั' comienza en 6
U+0E2A 'ส' comienza en 9
U+0E14 'ด' comienza en 12
U+0E35 'ี' comienza en 15

Usando DecodeRuneInString
U+0E2A 'ส' comienza en 0
encontrado so sua
U+0E27 'ว' comienza en 3
U+0E31 'ั' comienza en 6
U+0E2A 'ส' comienza en 9
encontrado so sua
U+0E14 'ด' comienza en 12
U+0E35 'ี' comienza en 15
```
