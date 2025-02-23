# Formateo de Cadenas

Se te pide formatear diferentes tipos de datos utilizando varios verbos de formateo en Golang.

## Requisitos

- Debes utilizar el paquete `fmt` para formatear los datos.
- Debes utilizar el verbo de formateo correcto para cada tipo de dato.
- Debes ser capaz de formatear enteros, flotantes, cadenas y structs.
- Debes ser capaz de controlar el ancho y la precisión de la salida.
- Debes ser capaz de justificar a la izquierda o a la derecha la salida.

## Ejemplo

```sh
$ go run string-formatting.go
struct1: {1 2}
struct2: {x:1 y:2}
struct3: main.point{x:1, y:2}
tipo: main.point
bool: true
int: 123
bin: 1110
char:!
hex: 1c8
float1: 78.900000
float2: 1.234000e+08
float3: 1.234000E+08
str1: "string"
str2: "\"string\""
str3: 6865782074686973
puntero: 0xc0000ba000
ancho1: | 12 | 345 \
  | ancho2: | 1.20 | 3.45 \
  | ancho3: | 1.20 | 3.45 \
  | ancho4: | foo | b \
  | ancho5: | foo | b \
  | sprintf: una cadena
io: un error
```
