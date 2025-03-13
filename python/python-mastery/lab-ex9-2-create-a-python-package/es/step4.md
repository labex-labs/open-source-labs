# Actualización y prueba del programa stock.py

Ahora que hemos creado nuestro paquete y corregido las importaciones internas, es hora de actualizar el archivo `stock.py` para utilizar nuestra nueva estructura de paquete. Un paquete en Python es una forma de organizar módulos relacionados juntos. Ayuda a mantener tu base de código organizada y facilita la gestión y reutilización del código.

Abre el archivo `stock.py` en el editor:

```bash
# Click on stock.py in the file explorer or run:
code stock.py
```

Las importaciones actuales en `stock.py` se basan en la estructura antigua en la que todos los archivos estaban en el mismo directorio. En Python, cuando importas un módulo, Python busca el módulo en ubicaciones específicas. En la estructura antigua, dado que todos los archivos estaban en el mismo directorio, Python podía encontrar fácilmente los módulos. Pero ahora, con la nueva estructura de paquete, necesitamos actualizar las importaciones para decirle a Python dónde encontrar los módulos dentro del paquete `structly`.

Actualiza el archivo `stock.py` para que se vea exactamente así:

```python
# stock.py

from structly.structure import Structure, String, PositiveInteger, PositiveFloat

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares

if __name__ == '__main__':
    from structly.reader import read_csv_as_instances
    from structly.tableformat import create_formatter, print_table
    portfolio = read_csv_as_instances('portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
```

Los cambios clave son:

1. Cambiado `from structure import Structure, String, PositiveInteger, PositiveFloat` a `from structly.structure import Structure, String, PositiveInteger, PositiveFloat`. Este cambio le dice a Python que busque el módulo `structure` dentro del paquete `structly`.
2. Cambiado `from reader import read_csv_as_instances` a `from structly.reader import read_csv_as_instances`. De manera similar, este cambio dirige a Python a encontrar el módulo `reader` dentro del paquete `structly`.
3. Cambiado `from tableformat import create_formatter, print_table` a `from structly.tableformat import create_formatter, print_table`. Esto asegura que Python localice el módulo `tableformat` en el paquete `structly`.

Guarda el archivo después de hacer estos cambios. Guardar el archivo es importante porque se asegura de que los cambios que has realizado se almacenen y se puedan utilizar cuando ejecutes el programa.

Ahora, probemos nuestro código actualizado para asegurarnos de que todo funcione correctamente:

```bash
python stock.py
```

Deberías ver la siguiente salida:

```
      name      shares       price
---------- ---------- ----------
      MSFT        100      51.23
       IBM         50       91.1
      AAPL         75     145.89
      ACME        125     123.45
       HPE         75       32.2
```

Si ves esta salida, ¡felicidades! Has creado con éxito un paquete de Python y actualizado tu código para utilizarlo. Esto significa que tu código ahora está organizado de manera más modular, lo que facilita su mantenimiento y expansión en el futuro.
