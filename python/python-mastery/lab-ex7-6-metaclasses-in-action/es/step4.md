# Prueba de nuestra implementación

Ahora que hemos implementado nuestra metaclase y modificado la clase `Structure`, es hora de probar nuestra implementación. Las pruebas son cruciales porque nos ayudan a asegurarnos de que todo funciona correctamente. Al ejecutar pruebas, podemos detectar cualquier problema potencial desde el principio y asegurarnos de que nuestro código se comporte como se espera.

Primero, ejecutemos las pruebas unitarias para ver si nuestra clase `Stock` funciona como se espera. Las pruebas unitarias son pruebas pequeñas y aisladas que verifican partes individuales de nuestro código. En este caso, queremos asegurarnos de que la clase `Stock` funcione correctamente. Para ejecutar las pruebas unitarias, usaremos el siguiente comando en la terminal:

```bash
python3 teststock.py
```

Si todo funciona correctamente, todas las pruebas deberían pasar sin errores. Cuando las pruebas se ejecutan con éxito, la salida debería verse algo así:

```
........
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

Los puntos representan cada prueba que pasó, y el `OK` final indica que todas las pruebas fueron exitosas.

Ahora, probemos nuestra clase `Stock` con algunos datos reales y la funcionalidad de formato de tablas. Esto nos dará un escenario más real para ver cómo interactúa nuestra clase `Stock` con los datos y cómo funciona el formato de tablas. Usaremos el siguiente comando en la terminal:

```bash
python3 -c "
from stock import Stock
from reader import read_csv_as_instances
from tableformat import create_formatter, print_table

# Read portfolio data into Stock instances
portfolio = read_csv_as_instances('portfolio.csv', Stock)
print('Portfolio:')
print(portfolio)

# Format and print the portfolio data
print('\nFormatted table:')
formatter = create_formatter('text')
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

En este código, primero importamos las clases y funciones necesarias. Luego leemos datos de un archivo CSV en instancias de `Stock`. Después, imprimimos los datos del portafolio y luego los formateamos en una tabla y la imprimimos.

Deberías ver una salida similar a esta:

```
Portfolio:
[Stock('AA',100,32.2), Stock('IBM',50,91.1), Stock('CAT',150,83.44), Stock('MSFT',200,51.23), Stock('GE',95,40.37), Stock('MSFT',50,65.1), Stock('IBM',100,70.44)]

Formatted table:
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

Tómese un momento para apreciar lo que hemos logrado:

1. Hemos creado un mecanismo para recopilar automáticamente todos los tipos de validadores. Esto significa que no tenemos que realizar un seguimiento manual de todos los validadores, lo que nos ahorra tiempo y reduce la posibilidad de errores.
2. Hemos implementado una metaclase que inyecta estos tipos en el espacio de nombres de las subclases de `Structure`. Esto permite que las subclases utilicen estos validadores sin tener que importarlos explícitamente.
3. Hemos eliminado la necesidad de importaciones explícitas de tipos de validadores. Esto hace que nuestro código sea más limpio y fácil de leer.
4. Todo esto sucede en segundo plano, lo que hace que el código para definir nuevas estructuras sea limpio y simple.

El archivo final `stock.py` es notablemente limpio en comparación con lo que habría sido sin nuestra metaclase:

```python
from structure import Structure

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

Sin necesidad de importar directamente los tipos de validadores, el código es más conciso y fácil de mantener. Este es un gran ejemplo de cómo las metaclases pueden mejorar la calidad de nuestro código.
