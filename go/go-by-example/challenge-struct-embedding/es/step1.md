# Incrustación de structs

Crea un struct llamado `container` que incorpore un struct llamado `base`. El struct `base` debe tener un campo llamado `num` de tipo `int` y un método llamado `describe()` que devuelva una cadena. El struct `container` debe tener un campo llamado `str` de tipo `string`. El struct `container` debe ser capaz de acceder al campo `num` y al método `describe()` del struct `base`.

## Requisitos

- El struct `base` debe tener un campo llamado `num` de tipo `int`.
- El struct `base` debe tener un método llamado `describe()` que devuelva una cadena.
- El struct `container` debe tener un campo llamado `str` de tipo `string`.
- El struct `container` debe incrustar el struct `base`.
- El struct `container` debe ser capaz de acceder al campo `num` y al método `describe()` del struct `base`.

## Ejemplo

```sh
$ go run struct-embedding.go
co={num: 1, str: algún nombre}
también num: 1
describe: base con num=1
describer: base con num=1
```
