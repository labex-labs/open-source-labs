# Validación de BST

## Problema

El problema consiste en escribir una función de Python que tome como entrada el nodo raíz de un árbol binario y determine si es un árbol de búsqueda binaria válido. Un árbol binario es un árbol de búsqueda binaria válido si y solo si se cumplen las siguientes condiciones:

1. El subárbol izquierdo de un nodo contiene solo nodos con valores menores que el valor del nodo.
2. El subárbol derecho de un nodo contiene solo nodos con valores mayores que el valor del nodo.
3. Tanto el subárbol izquierdo como el derecho son ellos mismos árboles de búsqueda binarios válidos.

## Requisitos

Para resolver este desafío, deben cumplirse los siguientes requisitos:

- La función debe ser capaz de manejar árboles binarios con duplicados.
- Si la función se llama con una entrada None, debe generar una excepción.
- La clase Node debe ya estar definida.
- El árbol binario debe caber en memoria.

## Uso de ejemplo

```txt
Válido:
      5
    /   \
   5     8
  /     /
 4     6
        \
         7

Inválido:
      5
    /   \
   5     8
  / \   /
 4   9 7
```
