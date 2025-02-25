# Hanói

## Problema

Tu tarea es implementar las Torres de Hanói con 3 torres y N discos. El objetivo es mover todos los discos de la primera torre a la tercera torre, cumpliendo las siguientes reglas simples:

1. Solo se puede mover un disco a la vez.
2. Cada movimiento consiste en tomar el disco superior de una de las pilas y colocarlo encima de otra pila o en una varilla vacía.
3. Ningún disco puede ser colocado encima de un disco más pequeño.

## Requisitos

Para resolver este problema, debes cumplir con los siguientes requisitos:

- Deberías tener una clase de pila que se pueda utilizar para este problema.
- Debes validar las entradas antes de procesarlas.
- Debes asegurar que el programa quepa en memoria.

## Uso de ejemplo

A continuación se presentan algunos ejemplos de cómo debería comportarse el programa:

- Si no hay torres, se debe generar una excepción.
- Si hay 0 discos, el programa debe devolver None.
- Si solo hay 1 disco, el programa debe moverlo de la primera torre a la tercera torre.
- Si hay 2 o más discos, el programa debe moverlos de la primera torre a la tercera torre, cumpliendo las reglas mencionadas anteriormente.
