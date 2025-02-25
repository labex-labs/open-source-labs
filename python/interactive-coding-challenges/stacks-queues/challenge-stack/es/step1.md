# Pila

## Problema

Implementa una pila utilizando una lista enlazada en Python, con los siguientes métodos:

- push: agrega un elemento en la cima de la pila
- pop: elimina y devuelve el elemento en la cima de la pila. Si la pila está vacía, devuelve None.
- peek: devuelve el elemento en la cima de la pila sin eliminarlo. Si la pila está vacía, devuelve None.
- is_empty: devuelve True si la pila está vacía, False en caso contrario.

## Requisitos

Los siguientes requisitos deben cumplirse:

- Al desapilar una pila vacía, devolver None.
- La implementación debe utilizar una lista enlazada.
- La implementación debe ser en Python.
- La implementación debe incluir los cuatro métodos: push, pop, peek y is_empty.

## Uso de ejemplo

### Push

- Apilar en pila vacía: stack.push(1)
- Apilar en pila no vacía: stack.push(2)

### Pop

- Desapilar en pila vacía: stack.pop() -> None
- Desapilar en pila con un solo elemento: stack.pop() -> 1
- Desapilar en pila con múltiples elementos: stack.pop() -> 2

### Peek

- Mirar en pila vacía: stack.peek() -> None
- Mirar en pila con un o más elementos: stack.peek() -> 2

### Is Empty

- Estar vacío en pila vacía: stack.is_empty() -> True
- Estar vacío en pila con un o más elementos: stack.is_empty() -> False
