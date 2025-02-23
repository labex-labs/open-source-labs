# Cartes

Dans ce défi, vous devrez créer une carte qui stocke le nombre de fois où chaque mot apparaît dans une chaîne de caractères donnée. Vous devrez diviser la chaîne en mots, puis itérer sur chaque mot, l'ajoutant à la carte s'il n'existe pas déjà, ou incrémentant son compte s'il existe déjà.

## Exigences

- Vous devez utiliser une carte pour stocker les comptes de mots.
- Vous devez diviser la chaîne d'entrée en mots.
- Vous devez itérer sur chaque mot dans la chaîne d'entrée.
- Vous devez ajouter chaque mot à la carte s'il n'existe pas déjà, ou incrémenter son compte s'il existe déjà.

## Exemple

```sh
# Notez que les cartes apparaissent sous la forme `map[k:v k:v]` lorsque
# elles sont imprimées avec `fmt.Println`.
$ go run maps.go
carte : map[k1:7 k2:13]
v1: 7
v3: 0
longueur : 2
carte : map[k1:7]
prs: faux
carte : map[bar:2 foo:1]
```
