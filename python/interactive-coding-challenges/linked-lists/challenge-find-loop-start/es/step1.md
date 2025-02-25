# Encontrar el inicio del ciclo

## Problema

Dada una lista enlazada simple, necesitamos encontrar el inicio de un ciclo si existe. Un ciclo se define como un nodo en la lista que apunta a un nodo previo, creando un ciclo. Si no hay ciclo, devolvemos `None`. Si hay un ciclo, devolvemos el nodo donde comienza el ciclo.

## Requisitos

Para resolver este problema, debemos considerar los siguientes requisitos:

- La lista enlazada es una lista enlazada simple.
- No podemos asumir que siempre se nos pasa una lista enlazada circular.
- Cuando encontramos un ciclo, devolvemos el nodo donde comienza el ciclo.
- Podemos asumir que ya tenemos una clase de lista enlazada que se puede utilizar para este problema.

## Uso de ejemplo

A continuación, se presentan algunos ejemplos de cómo se puede utilizar esta función:

- Lista vacía -> `None`
- No es una lista enlazada circular -> `None`
  - Un solo elemento
  - Dos o más elementos
- Caso general de lista enlazada circular
