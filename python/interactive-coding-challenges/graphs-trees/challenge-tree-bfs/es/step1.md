# Recorrido en anchura del árbol

## Problema

Dado un árbol binario, implementa una función que realice un recorrido en anchura en el árbol. La función debe llamar a un método de entrada `visit_func` en cada nodo cuando se procesa.

## Requisitos

Para resolver este problema, deben cumplirse los siguientes requisitos:

- Ya está disponible una clase `Node` con un método `insert`.
- La solución debe caber en memoria.
- El método `visit_func` debe ser llamado en cada nodo cuando se procesa.

## Ejemplo

### Recorrido en anchura

Supongamos que tenemos un árbol binario con la siguiente estructura:

```
    5
   / \
  2   8
 / \
1   3
```

Realizar un recorrido en anchura en este árbol resultaría en la siguiente secuencia de nodos visitados: `5, 2, 8, 1, 3`.
