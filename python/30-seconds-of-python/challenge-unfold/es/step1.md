# Desplegar lista

## Problema

Tu tarea es implementar la función `unfold` que toma una función iteradora y un valor semilla inicial como argumentos. La función iteradora acepta un solo argumento (`seed`) y siempre debe devolver una lista con dos elementos ([`valor`, `siguienteSemilla`]) o `False` para terminar. La función `unfold` debe utilizar una función generadora, `fn_generator`, que utilice un bucle `while` para llamar a la función iteradora y `generar` el `valor` hasta que devuelva `False`. Finalmente, la función `unfold` debe utilizar una comprensión de lista para devolver la lista que es producida por el generador, utilizando la función iteradora.

Implementa la función `unfold`:

```python
def unfold(fn, seed):
    # tu código aquí
```

### Entrada

- Una función iteradora `fn` que acepta un solo argumento (`seed`) y siempre debe devolver una lista con dos elementos ([`valor`, `siguienteSemilla`]) o `False` para terminar.
- Un valor semilla inicial `seed`.

### Salida

- Una lista que es producida por el generador, utilizando la función iteradora.

## Ejemplo

```python
f = lambda n: False if n > 50 else [-n, n + 10]
assert unfold(f, 10) == [-10, -20, -30, -40, -50]
```
