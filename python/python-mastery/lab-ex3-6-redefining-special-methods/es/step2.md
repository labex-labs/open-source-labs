# Haciendo objetos comparables con `__eq__`

En Python, cuando se utiliza el operador `==` para comparar dos objetos, Python en realidad llama al método especial `__eq__`. Por defecto, este método compara las identidades de los objetos, lo que significa que verifica si se almacenan en la misma dirección de memoria, en lugar de comparar su contenido.

Veamos un ejemplo. Supongamos que tenemos una clase `Stock`, y creamos dos objetos `Stock` con los mismos valores. Luego intentamos compararlos utilizando el operador `==`. Así es como se puede hacer en el intérprete de Python:

Primero, inicia el intérprete de Python ejecutando el siguiente comando en tu terminal:

```bash
python3
```

Luego, en el intérprete de Python, ejecuta el siguiente código:

```python
>>> import stock
>>> a = stock.Stock('GOOG', 100, 490.1)
>>> b = stock.Stock('GOOG', 100, 490.1)
>>> a == b
False
```

Como se puede ver, aunque los dos objetos `Stock` `a` y `b` tienen los mismos valores para sus atributos (`name`, `shares` y `price`), Python los considera objetos diferentes porque se almacenan en diferentes ubicaciones de memoria.

Para solucionar este problema, podemos implementar el método `__eq__` en nuestra clase `Stock`. Este método se llamará cada vez que se utilice el operador `==` en objetos de la clase `Stock`.

Ahora, abre el archivo `stock.py` nuevamente. Dentro de la clase `Stock`, agrega el siguiente método `__eq__`:

```python
def __eq__(self, other):
    return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                         (other.name, other.shares, other.price))
```

Analicemos lo que hace este método:

1. Primero, utiliza la función `isinstance` para verificar si el objeto `other` es una instancia de la clase `Stock`. Esto es importante porque solo queremos comparar objetos `Stock` con otros objetos `Stock`.
2. Si `other` es un objeto `Stock`, luego compara los atributos (`name`, `shares` y `price`) de ambos objetos, `self` y `other`.
3. Devuelve `True` solo si ambos objetos son instancias de `Stock` y sus atributos son idénticos.

Después de agregar el método `__eq__`, tu clase `Stock` completa debería verse así:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares -= shares

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"

    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                             (other.name, other.shares, other.price))
```

Ahora, probemos nuestra clase `Stock` mejorada. Inicia el intérprete de Python nuevamente:

```bash
python3
```

Luego, ejecuta el siguiente código en el intérprete de Python:

```python
>>> import stock
>>> a = stock.Stock('GOOG', 100, 490.1)
>>> b = stock.Stock('GOOG', 100, 490.1)
>>> a == b
True
>>> c = stock.Stock('GOOG', 200, 490.1)
>>> a == c
False
```

¡Genial! Ahora nuestros objetos `Stock` se pueden comparar adecuadamente según su contenido, en lugar de sus direcciones de memoria.

La comprobación `isinstance` en el método `__eq__` es crucial. Asegura que solo estemos comparando objetos `Stock`. Si no tuviéramos esta comprobación, comparar un objeto `Stock` con algo que no es un objeto `Stock` podría generar errores.

Cuando hayas terminado de probar, puedes salir del intérprete de Python ejecutando el siguiente comando:

```python
>>> exit()
```
