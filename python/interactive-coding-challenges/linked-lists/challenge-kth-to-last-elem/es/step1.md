# K-ésimo elemento contando desde el final

## Problema

Dada una lista enlazada simple no circular, la tarea es encontrar el k-ésimo elemento contando desde el final de la lista. Si k es 0, se debe devolver el último elemento. Si k es mayor o igual que la longitud de la lista enlazada, se debe devolver None. No se pueden utilizar estructuras de datos adicionales, y se asume que ya está disponible una clase de lista enlazada.

## Requisitos

Para resolver este problema, deben cumplirse los siguientes requisitos:

- La lista enlazada es simple y no circular.
- k es un entero válido.
- Si k es 0, se debe devolver el último elemento.
- Si k es mayor o igual que la longitud de la lista enlazada, se debe devolver None.
- No se pueden utilizar estructuras de datos adicionales.
- Ya está disponible una clase de lista enlazada.

## Uso de ejemplo

Los siguientes escenarios se pueden utilizar para probar la solución:

- Una lista vacía debe devolver None.
- Si k es mayor o igual que la longitud de la lista enlazada, se debe devolver None.
- Si la lista enlazada tiene un solo elemento y k es 0, se debe devolver el elemento.
- En un caso general con muchos elementos, donde k es menor que la longitud de la lista enlazada, se debe devolver el k-ésimo elemento contando desde el final.
