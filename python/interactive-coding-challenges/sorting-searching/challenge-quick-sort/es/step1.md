# Quick Sort

## Problema

Implementar el algoritmo Quick Sort en Python. El algoritmo debe tomar una lista no ordenada como entrada y devolver una lista ordenada. El algoritmo debe funcionar para listas de cualquier tamaño, incluyendo listas vacías y listas con elementos duplicados. El algoritmo también debe manejar la entrada no válida de manera adecuada.

El algoritmo Quick Sort funciona de la siguiente manera:

1. Elegir un elemento pivote de la lista.
2. Particionar la lista en dos sub-listas: una con elementos menores que el pivote y otra con elementos mayores que el pivote.
3. Aplicar recursivamente el algoritmo Quick Sort a las sub-listas.
4. Concatenar las sub-listas ordenadas con el elemento pivote en el medio.

## Requisitos

Para implementar el algoritmo Quick Sort en Python, deben cumplirse los siguientes requisitos:

- El algoritmo no debe ser una solución in-place.
- El algoritmo debe manejar los elementos duplicados en la lista.
- El algoritmo debe manejar la entrada no válida, como None o entrada no lista.
- El algoritmo debe ser capaz de manejar listas de cualquier tamaño, incluyendo listas vacías.

## Uso de ejemplo

Los siguientes son algunos ejemplos de cómo usar el algoritmo Quick Sort en Python:

- None -> Excepción

```python
quick_sort(None)
```

- Entrada vacía -> []

```python
quick_sort([])
```

- Un elemento -> [elemento]

```python
quick_sort([5])
```

- Dos o más elementos

```python
quick_sort([5, 2, 8, 3, 1, 9])
```
