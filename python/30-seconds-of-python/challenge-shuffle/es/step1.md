# Barajar una lista

## Problema

Escribe una función `shuffle(lst)` que tome una lista como entrada y devuelva una nueva lista con los mismos elementos en un orden aleatorizado. Tu función debe utilizar el algoritmo de Fisher-Yates para barajar los elementos de la lista.

El algoritmo de Fisher-Yates funciona de la siguiente manera:

1. Comienza con el último elemento de la lista.
2. Genera un índice aleatorio entre 0 y el índice actual.
3. Intercambia el elemento en el índice actual con el elemento en el índice aleatorio.
4. Avanza al siguiente elemento de la lista y repite los pasos 2-3 hasta que todos los elementos hayan sido barajados.

Tu función no debe modificar la lista original. En su lugar, debe crear una nueva lista con los elementos barajados.

Puedes suponer que la lista de entrada contendrá al menos un elemento.

## Ejemplo

```python
foo = [1, 2, 3, 4, 5]
shuffled_foo = shuffle(foo)
print(shuffled_foo) # [3, 1, 4, 5, 2]
print(foo) # [1, 2, 3, 4, 5]
```
