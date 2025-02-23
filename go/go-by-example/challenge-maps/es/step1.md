# Maps

En este desafío, necesitarás crear un mapa que almacene la cantidad de veces que cada palabra aparece en una cadena dada. Necesitarás dividir la cadena en palabras y luego iterar sobre cada palabra, agregándola al mapa si no existe o incrementando su contador si ya existe.

## Requisitos

- Debes usar un mapa para almacenar los conteos de palabras.
- Debes dividir la cadena de entrada en palabras.
- Debes iterar sobre cada palabra en la cadena de entrada.
- Debes agregar cada palabra al mapa si no existe o incrementar su contador si ya existe.

## Ejemplo

```sh
# Tenga en cuenta que los mapas aparecen en la forma `map[k:v k:v]` cuando
# se imprime con `fmt.Println`.
$ go run maps.go
map: map[k1:7 k2:13]
v1: 7
v3: 0
len: 2
map: map[k1:7]
prs: false
map: map[bar:2 foo:1]
```
