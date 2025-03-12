# Comprendiendo los métodos enlazados en Python

En Python, los métodos son un tipo especial de atributos que se pueden llamar. Cuando accedes a un método a través de un objeto, obtienes lo que llamamos un "método enlazado". Un método enlazado es esencialmente un método que está vinculado a un objeto específico. Esto significa que tiene acceso a los datos del objeto y puede operar sobre ellos.

## Accediendo a métodos como atributos

Comencemos a explorar los métodos enlazados utilizando nuestra clase `Stock`. Primero, veremos cómo acceder a un método como atributo de un objeto.

```python
# Open a Python interactive shell
python3

# Import the Stock class and create a stock object
from stock import Stock
s = Stock('GOOG', 100, 490.10)

# Access the cost method without calling it
cost_method = s.cost
print(cost_method)  # Output: <bound method Stock.cost of <stock.Stock object at 0x...>>

# Call the method
result = cost_method()
print(result)  # Output: 49010.0

# You can also do this in one step
print(s.cost())  # Output: 49010.0
```

En el código anterior, primero importamos la clase `Stock` y creamos una instancia de ella. Luego accedemos al método `cost` del objeto `s` sin llamarlo realmente. Esto nos da un método enlazado. Cuando llamamos a este método enlazado, calcula el costo basado en los datos del objeto. También puedes llamar directamente al método en el objeto en un solo paso.

## Usando getattr() con métodos

Otra forma de acceder a métodos es utilizando la función `getattr()`. Esta función te permite obtener un atributo de un objeto por su nombre.

```python
# Get the cost method using getattr
cost_method = getattr(s, 'cost')
print(cost_method)  # Output: <bound method Stock.cost of <stock.Stock object at 0x...>>

# Call the method
result = cost_method()
print(result)  # Output: 49010.0

# Get and call in one step
result = getattr(s, 'cost')()
print(result)  # Output: 49010.0
```

Aquí, usamos `getattr()` para obtener el método `cost` del objeto `s`. Al igual que antes, podemos llamar al método enlazado para obtener el resultado. E incluso puedes obtener y llamar al método en una sola línea.

## El método enlazado y su objeto

Un método enlazado siempre mantiene una referencia al objeto desde el que se accedió. Esto significa que incluso si almacenas el método en una variable, todavía sabe a qué objeto pertenece y puede acceder a los datos del objeto.

```python
# Store the cost method in a variable
c = s.cost

# Call the method
print(c())  # Output: 49010.0

# Change the object's state
s.shares = 75

# Call the method again - it sees the updated state
print(c())  # Output: 36757.5
```

En este ejemplo, almacenamos el método `cost` en una variable `c`. Cuando llamamos a `c()`, calcula el costo basado en los datos actuales del objeto. Luego cambiamos el atributo `shares` del objeto `s`. Cuando llamamos a `c()` de nuevo, utiliza los datos actualizados para calcular el nuevo costo.

## Explorando los internos del método enlazado

Un método enlazado tiene dos atributos importantes que nos dan más información sobre él.

- `__self__`: Este atributo se refiere al objeto al que está enlazado el método.
- `__func__`: Este atributo es el objeto función real que representa el método.

```python
# Get the cost method
c = s.cost

# Examine the bound method attributes
print(c.__self__)  # Output: <stock.Stock object at 0x...>
print(c.__func__)  # Output: <function Stock.cost at 0x...>

# You can manually call the function with the object
print(c.__func__(c.__self__))  # Output: 36757.5 (same as c())
```

Aquí, accedemos a los atributos `__self__` y `__func__` del método enlazado `c`. Podemos ver que `__self__` es el objeto `s`, y `__func__` es la función `cost`. Incluso podemos llamar manualmente a la función pasando el objeto como argumento, y nos da el mismo resultado que llamar directamente al método enlazado.

## Ejemplo con un método que toma argumentos

Veamos cómo funcionan los métodos enlazados con un método que toma argumentos, como el método `sell()`.

```python
# Get the sell method
sell_method = s.sell

# Examine the method
print(sell_method)  # Output: <bound method Stock.sell of <stock.Stock object at 0x...>>

# Call the method with an argument
sell_method(25)
print(s.shares)  # Output: 50

# Call the method manually using __func__ and __self__
sell_method.__func__(sell_method.__self__, 10)
print(s.shares)  # Output: 40
```

En este ejemplo, obtenemos el método `sell` como un método enlazado. Cuando lo llamamos con un argumento, actualiza el atributo `shares` del objeto `s`. También podemos llamar manualmente al método utilizando los atributos `__func__` y `__self__`, pasando el argumento también.

Comprender los métodos enlazados te ayuda a entender cómo funciona el sistema de objetos de Python por debajo, lo que puede ser útil para la depuración, la metaprogramación y la creación de patrones de programación avanzados.
