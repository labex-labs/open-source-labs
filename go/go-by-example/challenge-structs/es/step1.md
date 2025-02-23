# Structs

En este desafío, debes completar la función `newPerson` que construye un nuevo struct de persona con el nombre dado. El tipo de struct `person` tiene los campos `name` y `age`.

## Requisitos

- El tipo de struct `person` debe tener los campos `name` y `age`.
- La función `newPerson` debe construir un nuevo struct de persona con el nombre dado.
- La función `newPerson` debe devolver un puntero al nuevo struct de persona creado.
- La función `main` debe imprimir lo siguiente:
  - Un nuevo struct con nombre "Bob" y edad 20.
  - Un nuevo struct con nombre "Alice" y edad 30.
  - Un nuevo struct con nombre "Fred" y edad 0.
  - Un puntero a un nuevo struct con nombre "Ann" y edad 40.
  - Un nuevo struct construido usando la función `newPerson` con nombre "Jon" y edad 42.
  - El campo `name` de un struct con nombre "Sean" y edad 50.
  - El campo `age` de un puntero a un struct con nombre "Sean" y edad 50.
  - El campo `age` de un puntero a un struct con nombre "Sean" y edad 50 después de que el campo `age` se haya actualizado a 51.

## Ejemplo

```sh
$ go run structs.go
{Bob 20}
{Alice 30}
{Fred 0}
&{Ann 40}
&{Jon 42}
Sean
50
51
```
