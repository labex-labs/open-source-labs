# Desafío de conversión a lista

## Problema

Escribe una función `cast_list(val)` que tome un valor como argumento y lo devuelva como una lista. Si el valor ya es una lista, devuélvala tal cual. Si el valor no es una lista pero es iterable, devuélvalo como una lista. Si el valor no es iterable, devuélvalo como una lista de un solo elemento.

## Ejemplo

```python
cast_list('foo') # ['foo']
cast_list([1]) # [1]
cast_list(('foo', 'bar')) # ['foo', 'bar']
```
