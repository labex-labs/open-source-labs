# Expandir una lista

## Problema

Escribe una función llamada `spread(arg)` que tome una lista como argumento y devuelva una nueva lista que contiene todos los elementos de la lista original, aplanada. Si un elemento de la lista original es una lista en sí misma, sus elementos deben agregarse a la nueva lista por separado. La función no debe modificar la lista original.

Para implementar la función, debes recorrer los elementos de la lista original y usar el operador de expansión para agregar los elementos a la nueva lista. Si un elemento es una lista, debes usar el método `extend()` para agregar sus elementos a la nueva lista. Si un elemento no es una lista, debes usar el método `append()` para agregarlo a la nueva lista.

## Ejemplo

```python
spread([1, 2, 3, [4, 5, 6], [7], 8, 9]) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
