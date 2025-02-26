# Vuelta a la clasificación de listas

Las listas se pueden clasificar _in-place_. Utilizando el método `sort`.

```python
s = [10,1,7,3]
s.sort() # s = [1,3,7,10]
```

Puedes clasificar en orden inverso.

```python
s = [10,1,7,3]
s.sort(reverse=True) # s = [10,7,3,1]
```

Parece bastante simple. Sin embargo, ¿cómo clasificamos una lista de diccionarios?

```python
[{'name': 'AA', 'price': 32.2,'shares': 100},
{'name': 'IBM', 'price': 91.1,'shares': 50},
{'name': 'CAT', 'price': 83.44,'shares': 150},
{'name': 'MSFT', 'price': 51.23,'shares': 200},
{'name': 'GE', 'price': 40.37,'shares': 95},
{'name': 'MSFT', 'price': 65.1,'shares': 50},
{'name': 'IBM', 'price': 70.44,'shares': 100}]
```

¿Por qué criterio?

Puedes guiar la clasificación utilizando una _función clave_. La _función clave_ es una función que recibe el diccionario y devuelve el valor de interés para la clasificación.

```python
portfolio = [
    {'name': 'AA', 'price': 32.2,'shares': 100},
    {'name': 'IBM', 'price': 91.1,'shares': 50},
    {'name': 'CAT', 'price': 83.44,'shares': 150},
    {'name': 'MSFT', 'price': 51.23,'shares': 200},
    {'name': 'GE', 'price': 40.37,'shares': 95},
    {'name': 'MSFT', 'price': 65.1,'shares': 50},
    {'name': 'IBM', 'price': 70.44,'shares': 100}
]

def stock_name(s):
    return s['name']

portfolio.sort(key=stock_name)
```

Aquí está el resultado.

```python
# Comprueba cómo se clasifican los diccionarios por la clave `name`
[
  {'name': 'AA', 'price': 32.2,'shares': 100},
  {'name': 'CAT', 'price': 83.44,'shares': 150},
  {'name': 'GE', 'price': 40.37,'shares': 95},
  {'name': 'IBM', 'price': 91.1,'shares': 50},
  {'name': 'IBM', 'price': 70.44,'shares': 100},
  {'name': 'MSFT', 'price': 51.23,'shares': 200},
  {'name': 'MSFT', 'price': 65.1,'shares': 50}
]
```
