# Lista de Cola

## Problema

Implementar una cola con métodos de encolar y desencolar utilizando una lista enlazada. El método de encolar debe agregar un elemento al final de la cola, y el método de desencolar debe eliminar un elemento del frente de la cola. Si la cola está vacía, desencolar debe devolver None.

## Requisitos

Para implementar la cola, debemos cumplir con los siguientes requisitos:

- Si hay un elemento en la lista, los punteros primero y último deben apuntar a él.
- Si no hay elementos en la lista, los punteros primero y último deben ser None.
- Si se desencola una cola vacía, debe devolver None.
- Podemos asumir que esto cabe en memoria.

## Uso de Ejemplo

### Encolar

- Encolar en una cola vacía: Si la cola está vacía, el método de encolar debe agregar el elemento como el primer y último elemento de la cola.
- Encolar en una cola no vacía: Si la cola no está vacía, el método de encolar debe agregar el elemento al final de la cola.

### Desencolar

- Desencolar una cola vacía -> None: Si la cola está vacía, el método de desencolar debe devolver None.
- Desencolar una cola con un elemento: Si la cola tiene solo un elemento, el método de desencolar debe eliminar el elemento y establecer los punteros primero y último en None.
- Desencolar una cola con más de un elemento: Si la cola tiene más de un elemento, el método de desencolar debe eliminar el primer elemento y establecer el puntero primero al siguiente elemento.
