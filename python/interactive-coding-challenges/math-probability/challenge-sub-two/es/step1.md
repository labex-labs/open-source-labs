# Restar dos números

## Problema

Escribe una función de Python que tome dos enteros como entrada y devuelva su diferencia sin utilizar el signo '+' o '-'. La función debe manejar los siguientes casos:

- Si cualquiera de las entradas es None, la función debe generar un TypeError.
- La función debe funcionar tanto para enteros positivos como negativos.

## Requisitos

Para resolver este problema, debemos cumplir con los siguientes requisitos:

- Comprobar si la entrada es None y generar un TypeError si es necesario.
- Podemos suponer que las entradas caben en la memoria.

## Uso de ejemplo

A continuación se muestran algunos ejemplos de cómo debe comportarse la función:

```
sub_two(None, 5) -> TypeError
sub_two(7, 5) -> 2
sub_two(-5, -7) -> 2
sub_two(-5, 7) -> -12
sub_two(5, -7) -> 12
```
