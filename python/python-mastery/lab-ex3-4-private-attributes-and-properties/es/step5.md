# Reconciliación de la Validación de Tipos con Variables de Clase

En nuestro viaje de programación en Python, hemos creado una clase `Stock`. Actualmente, esta clase tiene dos formas diferentes de manejar los tipos de datos. Comprender estos mecanismos es crucial, ya que nos ayuda a administrar y organizar mejor nuestro código.

El primer mecanismo es la variable de clase `_types`. Esta variable se utiliza para convertir datos de filas. Cuando obtenemos datos en formato de fila, la variable `_types` nos ayuda a transformar esos datos en los tipos adecuados para nuestra clase `Stock`.

El segundo mecanismo son los setters de propiedades. Estos setters aplican la comprobación de tipos. Siempre que intentamos establecer un valor para una propiedad en nuestra clase `Stock`, los setters de propiedades se aseguran de que el valor sea del tipo correcto.

Sin embargo, tener dos mecanismos separados puede hacer que nuestra clase sea difícil de mantener. Para resolver este problema, necesitamos reconciliar estos dos mecanismos para que utilicen la misma información de tipo. De esta manera, aseguramos la coherencia en nuestra clase y se vuelve más confiable cuando creamos subclases.

## Instrucciones:

1. Primero, necesitamos abrir el archivo `stock.py` en el editor. Este archivo contiene el código de nuestra clase `Stock`. Para abrirlo, ejecuta el siguiente comando en la terminal:

   ```bash
   code /home/labex/project/stock.py
   ```

2. Ahora, modificaremos los setters de propiedades en el archivo `stock.py`. Queremos que utilicen los tipos definidos en la variable de clase `_types`. Esto asegura que la comprobación de tipos en los setters de propiedades sea consistente con la conversión de tipos realizada por la variable `_types`. Así es como modificamos los setters de propiedades:

   ```python
   @property
   def shares(self):
       return self._shares

   @shares.setter
   def shares(self, value):
       if not isinstance(value, self._types[1]):
           raise TypeError(f"Expected {self._types[1].__name__}")
       if value < 0:
           raise ValueError("shares must be >= 0")
       self._shares = value

   @property
   def price(self):
       return self._price

   @price.setter
   def price(self, value):
       if not isinstance(value, self._types[2]):
           raise TypeError(f"Expected {self._types[2].__name__}")
       if value < 0:
           raise ValueError("price must be >= 0")
       self._price = value
   ```

3. Después de realizar estos cambios, guarda el archivo `stock.py`. Guardar el archivo asegura que nuestras modificaciones se conserven.

4. A continuación, crearemos un script de prueba para verificar que la creación de subclases con diferentes tipos funcione como se espera. Para crear este script, ejecuta el siguiente comando en la terminal:

   ```bash
   code /home/labex/project/test_subclass.py
   ```

5. Ahora, agrega el siguiente código al archivo `test_subclass.py`. Este código crea una subclase de la clase `Stock` con diferentes tipos y prueba tanto la clase base como la subclase.

   ```python
   from stock import Stock
   from decimal import Decimal

   # Create a subclass with different types
   class DStock(Stock):
       _types = (str, int, Decimal)

   # Test the base class
   s = Stock('GOOG', 100, 490.10)
   print(f"Stock: {s.name}, Shares: {s.shares}, Price: {s.price}, Cost: {s.cost}")

   # Test valid update with float
   try:
       s.price = 500.25
       print(f"Updated Stock price: {s.price}, Cost: {s.cost}")
   except Exception as e:
       print(f"Error updating Stock price: {e}")

   # Test the subclass with Decimal
   ds = DStock('AAPL', 50, Decimal('142.50'))
   print(f"DStock: {ds.name}, Shares: {ds.shares}, Price: {ds.price}, Cost: {ds.cost}")

   # Test invalid update with float (should require Decimal)
   try:
       ds.price = 150.75
       print(f"Updated DStock price: {ds.price}")
   except Exception as e:
       print(f"Error updating DStock price: {e}")

   # Test valid update with Decimal
   try:
       ds.price = Decimal('155.25')
       print(f"Updated DStock price: {ds.price}, Cost: {ds.cost}")
   except Exception as e:
       print(f"Error updating DStock price: {e}")
   ```

6. Finalmente, ejecuta el script de prueba para ver los resultados. Ejecuta el siguiente comando en la terminal:

   ```bash
   python /home/labex/project/test_subclass.py
   ```

Cuando ejecutes el script de prueba, deberías ver que la clase base `Stock` acepta valores de tipo float para el precio, mientras que la subclase `DStock` requiere valores de tipo `Decimal`. Esto muestra que nuestra reconciliación de tipos funcionó como se esperaba.

### Discusión

Al reconciliar la información de tipo en nuestra clase `Stock`, hemos hecho que la clase sea más consistente. Ahora, los setters de propiedades utilizan la misma información de tipo que el método `from_row`. Esta coherencia hace que la clase sea más fácil de mantener y extender, especialmente cuando se crean subclases.

Aunque la implementación actual de nuestra clase `Stock` puede parecer compleja para un concepto simple, demuestra técnicas importantes de Python para la encapsulación y la seguridad de tipos. En aplicaciones del mundo real, es posible que desees utilizar herramientas más avanzadas como dataclasses o bibliotecas de terceros para simplificar este tipo de implementación. Estas herramientas pueden hacer que tu código sea más conciso y fácil de administrar.
