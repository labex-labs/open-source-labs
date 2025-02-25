# Cola de prioridad

## Problema

Implementar una cola de prioridad respaldada por una matriz. La cola de prioridad debe soportar los siguientes métodos:

- `insert`: insertar un nuevo elemento en la cola de prioridad
- `extract_min`: eliminar y devolver el elemento mínimo de la cola de prioridad
- `decrease_key`: disminuir la clave de un elemento dado en la cola de prioridad

## Requisitos

Para implementar la cola de prioridad, debemos cumplir con los siguientes requisitos:

- Los métodos soportados por la cola de prioridad deben ser `insert`, `extract_min` y `decrease_key`.
- No habrá claves duplicadas en la cola de prioridad.
- No necesitamos validar las entradas.
- La cola de prioridad debe caber en memoria.

## Uso de ejemplo

A continuación se presentan algunos ejemplos de cómo utilizar los métodos de la cola de prioridad:

### insert

- `insert` caso general: insertar un nuevo nodo en la cola de prioridad.

### extract_min

- `extract_min` de una lista vacía: devolver None.
- `extract_min` caso general: eliminar y devolver el nodo mínimo de la cola de prioridad.

### decrease_key

- `decrease_key` una clave no válida: devolver None.
- `decrease_key` caso general: disminuir la clave de un nodo dado en la cola de prioridad.
