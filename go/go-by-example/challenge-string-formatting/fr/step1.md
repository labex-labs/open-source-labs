# Formatage de chaînes de caractères

Vous êtes requis de formater différents types de données à l'aide de divers verbes de formatage en Golang.

## Exigences

- Vous devez utiliser le package `fmt` pour formater les données.
- Vous devez utiliser le verbe de formatage correct pour chaque type de données.
- Vous devez être capable de formater des entiers, des flottants, des chaînes de caractères et des structs.
- Vous devez être capable de contrôler la largeur et la précision de la sortie.
- Vous devez être capable d'aligner à gauche ou à droite la sortie.

## Exemple

```sh
$ go run string-formatting.go
struct1: {1 2}
struct2: {x:1 y:2}
struct3: main.point{x:1, y:2}
type: main.point
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
pointer: 0xc0000ba000
width1: | 12 | 345 \
  | width2: | 1.20 | 3.45 \
  | width3: | 1.20 | 3.45 \
  | width4: | foo | b \
  | width5: | foo | b \
  | sprintf: a string
io: an error
```
