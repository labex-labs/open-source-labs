# Pila con mínimo

## Problema

El problema consiste en implementar una pila con métodos push, pop y min que funcionen en O(1) tiempo. El método push agrega un elemento a la colección, el método pop elimina el elemento más recientemente agregado que no ha sido eliminado aún, y el método min devuelve el elemento mínimo de la pila. Los tres métodos deben ejecutarse en tiempo constante, O(1).

## Requisitos

Para resolver este problema, debemos considerar los siguientes requisitos:

- La pila contiene solo enteros.
- Los valores de entrada para push son válidos.
- Si llamamos al método min en una pila vacía, deberíamos devolver sys.maxsize.
- Podemos suponer que ya tenemos una clase de pila que se puede utilizar para este problema.
- Podemos suponer que la pila cabe en memoria.

## Uso de ejemplo

Podemos probar nuestra implementación con los siguientes escenarios:

- Push/pop en una pila vacía.
- Push/pop en una pila no vacía.
- Min en una pila vacía.
- Min en una pila no vacía.
