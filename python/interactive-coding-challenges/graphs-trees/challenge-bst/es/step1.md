# Bst

## Problema

Un árbol binario de búsqueda es una estructura de datos que permite operaciones rápidas de búsqueda, inserción y eliminación. Es un árbol en el que cada nodo tiene como máximo dos hijos, y el hijo izquierdo es menor que el padre, y el hijo derecho es mayor que el padre. El método de inserción agrega un nuevo nodo al árbol en la posición adecuada según su valor.

Tu tarea es implementar un árbol binario de búsqueda con un método de inserción en Python. El método de inserción debe tomar un valor y agregar un nuevo nodo al árbol en la posición adecuada según su valor. Si la entrada de la raíz es None, devuelve un árbol con el único elemento siendo el nuevo nodo raíz.

## Requisitos

Para completar este desafío, debes cumplir con los siguientes requisitos:

- No se pueden insertar valores None.
- Puedes asumir que estás trabajando con enteros válidos.
- Puedes asumir que todos los descendientes izquierdos son menores o iguales que el nodo, y todos los descendientes derechos son mayores que el nodo.
- No tienes que llevar un registro de los nodos padre, pero es opcional.
- Puedes asumir que esto cabe en memoria.

## Uso de ejemplo

### Inserción

La inserción se probará a través de la siguiente recorrido:

### Recorrido In-Order

- 5, 2, 8, 1, 3 -> 1, 2, 3, 5, 8
- 1, 2, 3, 4, 5 -> 1, 2, 3, 4, 5

No tienes que codificar el recorrido in-order, es parte de la prueba unitaria.
