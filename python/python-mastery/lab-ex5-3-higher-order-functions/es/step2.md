# Mapeo

Una de las operaciones más comunes en la programación funcional es la operación `map()` que aplica una función a los valores de una secuencia. Python tiene una función `map()` incorporada que hace esto. Por ejemplo:

```python
>>> nums = [1,2,3,4]
>>> squares = map(lambda x: x*x, nums)
>>> for n in squares:
        print(n)

1
4
9
16
>>>
```

`map()` produce un iterador, por lo que si quieres una lista, tendrás que crearla explícitamente:

```python
>>> squares = list(map(lambda x: x*x, nums))
>>> squares
[1, 4, 9, 16]
>>>
```

Intenta usar `map()` en tu función `convert_csv()`.
