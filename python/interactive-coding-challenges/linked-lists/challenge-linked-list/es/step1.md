# Lista enlazada

## Problema

Implementar una lista enlazada con los siguientes métodos:

- insert(value): inserta un nuevo nodo con el valor dado al principio de la lista
- append(value): inserta un nuevo nodo con el valor dado al final de la lista
- find(value): devuelve el primer nodo de la lista con el valor dado, o None si no existe tal nodo
- delete(value): elimina el primer nodo de la lista con el valor dado, o no hace nada si no existe tal nodo
- length(): devuelve el número de nodos de la lista
- print(): imprime los valores de todos los nodos de la lista, separados por espacios

## Requisitos

La implementación de la lista enlazada debe cumplir los siguientes requisitos:

- La lista enlazada es no circular y simplemente enlazada.
- La implementación solo lleva un registro de la cabeza de la lista, no de la cola.
- No se pueden insertar valores None en la lista.

## Uso de ejemplo

### Insertar al principio

- Insertar un None: Lanza un error ya que no se pueden insertar valores None en la lista.
- Insertar en una lista vacía: Inserta el valor como el primer nodo de la lista.
- Insertar en una lista con un elemento o más elementos: Inserta el valor como el primer nodo de la lista, desplazando los nodos existentes hacia la derecha.

### Anexar

- Anexar un None: Lanza un error ya que no se pueden insertar valores None en la lista.
- Anexar en una lista vacía: Inserta el valor como el primer nodo de la lista.
- Anexar en una lista con un elemento o más elementos: Inserta el valor como el último nodo de la lista, actualizando la referencia del último nodo anterior para que apunte al nuevo nodo.

### Buscar

- Buscar un None: Devuelve None ya que no se pueden encontrar valores None en la lista.
- Buscar en una lista vacía: Devuelve None ya que no hay nodos en la lista.
- Buscar en una lista con un elemento o más elementos coincidentes: Devuelve el primer nodo de la lista con el valor dado.
- Buscar en una lista sin coincidencias: Devuelve None ya que no hay nodos en la lista con el valor dado.

### Eliminar

- Eliminar un None: No hace nada ya que no se pueden eliminar valores None de la lista.
- Eliminar en una lista vacía: No hace nada ya que no hay nodos en la lista.
- Eliminar en una lista con un elemento o más elementos coincidentes: Elimina el primer nodo de la lista con el valor dado, desplazando los nodos existentes hacia la izquierda.
- Eliminar en una lista sin coincidencias: No hace nada ya que no hay nodos en la lista con el valor dado.

### Longitud

- Longitud de cero o más elementos: Devuelve el número de nodos de la lista.

### Imprimir

- Imprimir una lista vacía: No imprime nada.
- Imprimir una lista con un elemento o más elementos: Imprime los valores de todos los nodos de la lista, separados por espacios.
