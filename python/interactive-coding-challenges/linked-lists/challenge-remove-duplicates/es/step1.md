# Eliminar duplicados

## Problema

Dada una lista enlazada simple no circular, elimine los duplicados de la misma. El objetivo es modificar la lista original in-place y devolver la cabeza de la lista modificada.

## Requisitos

Para resolver este problema, debemos considerar los siguientes requisitos:

- La lista enlazada es no circular y simple.
- No se pueden insertar valores nulos en la lista.
- Ya tenemos una clase de lista enlazada que se puede utilizar para este problema.
- Se deben implementar dos soluciones: una que utilice estructuras de datos adicionales y otra sin ellas.
- El problema cabe en memoria.

## Uso de ejemplo

A continuación se presentan algunos ejemplos de cómo debe comportarse la función:

- Lista enlazada vacía -> []
- Lista enlazada con un elemento -> [elemento]
- Caso general sin duplicados -> [1, 2, 3, 4]
- Caso general con duplicados -> [1, 2, 3]
