# Mejorando la representación de objetos con `__repr__`

En Python, los objetos se pueden representar como cadenas de dos maneras diferentes. Estas representaciones tienen diferentes propósitos y son útiles en diversos escenarios.

El primer tipo es la **representación como cadena**. Esta es creada por la función `str()`, que se llama automáticamente cuando se utiliza la función `print()`. La representación como cadena está diseñada para ser legible por humanos. Presenta el objeto en un formato que es fácil de entender e interpretar.

El segundo tipo es la **representación como código**. Esta es generada por la función `repr()`. La representación como código muestra el código que se necesitaría escribir para recrear el objeto. Se trata más de proporcionar una forma precisa y sin ambigüedades de representar el objeto en código.

Veamos un ejemplo concreto utilizando la clase `date` incorporada en Python. Esto te ayudará a ver la diferencia entre las representaciones como cadena y como código en acción.

```python
>>> from datetime import date
>>> d = date(2008, 7, 5)
>>> print(d)              # Uses str()
2008-07-05
>>> d                     # Uses repr()
datetime.date(2008, 7, 5)
```

En este ejemplo, cuando usamos `print(d)`, Python llama a la función `str()` en el objeto `date` `d`, y obtenemos una fecha legible por humanos en el formato `YYYY-MM-DD`. Cuando simplemente escribimos `d` en la shell interactiva, Python llama a la función `repr()`, y vemos el código necesario para recrear el objeto `date`.

Puedes obtener explícitamente la cadena de `repr()` de varias maneras. Aquí hay algunos ejemplos:

```python
>>> print('The date is', repr(d))
The date is datetime.date(2008, 7, 5)
>>> print(f'The date is {d!r}')
The date is datetime.date(2008, 7, 5)
>>> print('The date is %r' % d)
The date is datetime.date(2008, 7, 5)
```

Ahora, apliquemos este concepto a nuestra clase `Stock`. Vamos a mejorar la clase implementando el método `__repr__`. Este método especial es llamado por Python cuando necesita la representación como código de un objeto.

Para hacer esto, abre el archivo `stock.py` en tu editor. Luego, agrega el método `__repr__` a la clase `Stock`. El método `__repr__` debe devolver una cadena que muestre el código necesario para recrear el objeto `Stock`.

```python
def __repr__(self):
    return f"Stock('{self.name}', {self.shares}, {self.price})"
```

Después de agregar el método `__repr__`, tu clase `Stock` completa debería verse así:

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
```

Ahora, probemos nuestra clase `Stock` modificada. Abre una shell interactiva de Python ejecutando el siguiente comando en tu terminal:

```bash
python3
```

Una vez que la shell interactiva esté abierta, prueba los siguientes comandos:

```python
>>> import stock
>>> goog = stock.Stock('GOOG', 100, 490.10)
>>> goog
Stock('GOOG', 100, 490.1)
```

También puedes ver cómo funciona el método `__repr__` con una cartera de acciones. Aquí hay un ejemplo:

```python
>>> import reader
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> portfolio
[Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44), Stock('MSFT', 200, 51.23), Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.1), Stock('IBM', 100, 70.44)]
```

Como puedes ver, el método `__repr__` ha hecho que nuestros objetos `Stock` sean mucho más informativos cuando se muestran en la shell interactiva o en el depurador. Ahora muestra el código necesario para recrear cada objeto, lo cual es muy útil para depurar y entender el estado de los objetos.

Cuando hayas terminado de probar, puedes salir del intérprete de Python ejecutando el siguiente comando:

```python
>>> exit()
```
