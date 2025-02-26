# Pasando Tuplas y Diccionarios

Las tuplas se pueden expandir en argumentos variables.

```python
numbers = (2,3,4)
f(1, *numbers)      # Lo mismo que f(1,2,3,4)
```

Los diccionarios también se pueden expandir en argumentos de palabras clave.

```python
options = {
    'color' : 'rojo',
    'delimitador' : ',',
    'ancho' : 400
}
f(data, **options)
# Lo mismo que f(data, color='rojo', delimitador=',', ancho=400)
```
