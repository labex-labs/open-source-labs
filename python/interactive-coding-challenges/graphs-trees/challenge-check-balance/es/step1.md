# Comprobar el equilibrio

## Problema

Dado un árbol binario, escribe una función de Python para determinar si está equilibrado. Un árbol binario se considera equilibrado si las alturas de los dos subárboles de cualquier nodo difieren como máximo en uno. La función debe tomar el nodo raíz del árbol binario como entrada y devolver True si el árbol está equilibrado, y False en caso contrario. Si la entrada es None, la función debe generar una excepción.

## Requisitos

Para resolver este problema, debemos cumplir con los siguientes requisitos:

- Un árbol equilibrado es aquel en el que las alturas de los dos subárboles de cualquier nodo no difieren en más de 1.
- Si la entrada es None, la función debe generar una excepción.
- Podemos suponer que ya tenemos una clase Node con un método insert.
- Podemos suponer que el programa ajusta en memoria.

## Uso de ejemplo

A continuación se presentan algunos ejemplos de cómo debe comportarse la función:

- None -> generar una excepción
- 1 -> True
- 5, 3, 8, 1, 4 -> True
- 5, 3, 8, 9, 10 -> False
