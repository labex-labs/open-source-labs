# Chaînes de caractères et runes

Le problème à résoudre dans ce défi est de comprendre comment travailler avec les chaînes de caractères et les runes en Go. Plus précisément, le défi couvrira la manière d'obtenir la longueur d'une chaîne de caractères, d'accéder à un élément d'une chaîne de caractères, de compter le nombre de runes dans une chaîne de caractères et d'itérer sur les runes d'une chaîne de caractères.

## Exigences

Pour terminer ce défi, vous devrez :

- Avoir une compréhension de base de la syntaxe Go
- Connaître les chaînes de caractères et les runes en Go
- La bibliothèque standard Go

## Exemple

```sh
$ go run strings-and-runes.go
Longueur : 18
e0 b8 aa e0 b8 a7 e0 b8 b1 e0 b8 aa e0 b8 94 e0 b8 b5
Nombre de runes : 6
U+0E2A 'ส' commence à 0
U+0E27 'ว' commence à 3
U+0E31 'ั' commence à 6
U+0E2A 'ส' commence à 9
U+0E14 'ด' commence à 12
U+0E35 'ี' commence à 15

En utilisant DecodeRuneInString
U+0E2A 'ส' commence à 0
trouvé so sua
U+0E27 'ว' commence à 3
U+0E31 'ั' commence à 6
U+0E2A 'ส' commence à 9
trouvé so sua
U+0E14 'ด' commence à 12
U+0E35 'ี' commence à 15
```
