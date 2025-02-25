# Partición

## Problema

Dada una lista enlazada simple, partícilala alrededor de un valor x, de modo que todos los nodos menores que x queden antes que todos los nodos mayores o iguales a x. La función debe devolver una nueva lista enlazada.

## Requisitos

Para resolver este problema, debemos considerar los siguientes requisitos:

- La lista enlazada no es circular y es simple.
- La función debe devolver una nueva lista enlazada.
- El valor de entrada x es válido.
- Ya tenemos una clase de lista enlazada que se puede utilizar para este problema.
- Podemos crear estructuras de datos adicionales.
- El problema cabe en la memoria.

## Uso de ejemplo

A continuación se muestran algunos ejemplos de cómo debe funcionar la función:

- Lista vacía -> []
- Lista de un elemento -> [elemento]
- Lista izquierda vacía -> [10, 11, 12]
- Lista derecha vacía -> [1, 2, 3]
- Caso general
  - Partición = 10
  - Entrada: 4, 3, 7, 8, 10, 1, 10, 12
  - Salida: 4, 3, 7, 8, 1, 10, 10, 12
