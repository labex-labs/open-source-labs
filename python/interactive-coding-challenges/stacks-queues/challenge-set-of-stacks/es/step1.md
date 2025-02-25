# Conjunto de Pilas

## Problema

Implementar una clase SetOfStacks que envuelva una lista de pilas, donde cada pila está limitada por una capacidad. La clase debe tener las siguientes funcionalidades:

- Empujar un elemento hacia la cima de la última pila de la lista. Si la última pila está llena, crear una nueva pila y agregar el elemento a la nueva pila.
- Sacar el elemento superior de la última pila de la lista. Si la última pila está vacía, eliminarla de la lista y sacar el elemento superior de la nueva última pila de la lista. Si la lista está vacía, devolver None.
- Sacar un elemento de una pila específica de la lista. Si la pila está vacía, eliminarla de la lista. Si la lista está vacía, devolver None.

## Requisitos

La clase SetOfStacks debe cumplir con los siguientes requisitos:

- La clase debe utilizar una clase de pila existente.
- Todas las pilas de la lista deben estar limitadas por la misma capacidad.
- Si una pila se llena, se debe crear automáticamente una nueva pila para almacenar elementos adicionales.
- Si una pila se vacía, debe eliminarse de la lista.
- Si hacemos pop en una pila vacía, el método debe devolver None.
- La implementación debe caber en memoria.

## Uso de ejemplo

La clase SetOfStacks se puede utilizar en los siguientes escenarios:

- Empujar y sacar en una pila vacía.
- Empujar y sacar en una pila no vacía.
- Empujar en una pila con capacidad para crear una nueva.
- Sacar en una pila para destruirla.
