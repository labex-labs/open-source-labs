# Imbrication de structs

Créez un struct nommé `container` qui imbrique un struct nommé `base`. Le struct `base` devrait avoir un champ nommé `num` de type `int` et une méthode nommée `describe()` qui renvoie une chaîne de caractères. Le struct `container` devrait avoir un champ nommé `str` de type `string`. Le struct `container` devrait être capable d'accéder au champ `num` et à la méthode `describe()` du struct `base`.

## Exigences

- Le struct `base` devrait avoir un champ nommé `num` de type `int`.
- Le struct `base` devrait avoir une méthode nommée `describe()` qui renvoie une chaîne de caractères.
- Le struct `container` devrait avoir un champ nommé `str` de type `string`.
- Le struct `container` devrait imbriquer le struct `base`.
- Le struct `container` devrait être capable d'accéder au champ `num` et à la méthode `describe()` du struct `base`.

## Exemple

```sh
$ go run struct-embedding.go
co={num: 1, str: some name}
also num: 1
describe: base with num=1
describer: base with num=1
```
