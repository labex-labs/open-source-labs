# Cola a partir de Pilas

## Problema

Implementar una cola utilizando dos pilas puede ser un problema desafiante. La idea básica es utilizar una pila para las operaciones de encolar y la otra pila para las operaciones de desencolar. Cuando un elemento se encola, se empuja en la primera pila. Cuando un elemento se desencola, se saca de la segunda pila. Si la segunda pila está vacía, sacamos todos los elementos de la primera pila y los empujamos en la segunda pila en orden inverso. Esto garantiza que el primer elemento que se encoló sea el primer elemento que se desencola.

## Requisitos

Para resolver este problema, debemos considerar los siguientes requisitos:

- Debemos implementar dos métodos: encolar y desencolar.
- Debemos suponer que ya tenemos una clase de pila que se puede utilizar para este problema.
- No podemos empujar un valor nulo a la Pila.
- Podemos suponer que este problema cabe en la memoria.

## Uso de ejemplo

A continuación se presentan algunos ejemplos de cómo podemos utilizar nuestra implementación de una cola utilizando dos pilas:

- Encolar y desencolar en una pila vacía: podemos encolar un elemento en la cola y luego desencolarlo para asegurarnos de que la cola está funcionando correctamente.
- Encolar y desencolar en una pila no vacía: podemos encolar múltiples elementos en la cola y luego desencolarlos para asegurarnos de que la cola está funcionando correctamente.
- Varios encolar seguidos: podemos encolar múltiples elementos en la cola seguidos y luego desencolarlos para asegurarnos de que la cola está funcionando correctamente.
- Varios desencolar seguidos: podemos encolar múltiples elementos en la cola y luego desencolarlos seguidos para asegurarnos de que la cola está funcionando correctamente.
- Encolar después de un desencolar: podemos encolar un elemento en la cola, desencolarlo y luego encolar otro elemento en la cola para asegurarnos de que la cola está funcionando correctamente.
- Desencolar después de un encolar: podemos encolar un elemento en la cola, desencolarlo y luego encolar otro elemento en la cola para asegurarnos de que la cola está funcionando correctamente.
