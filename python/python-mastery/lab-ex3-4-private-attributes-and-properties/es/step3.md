# Implementación de Validación de Propiedades

Las propiedades en Python son una característica poderosa. No solo te permiten acceder a valores calculados como si fueran atributos normales, sino que también te dan control sobre cómo se recuperan, establecen y eliminan estos valores de atributos. Este control es extremadamente útil cuando necesitas agregar validación a tus atributos. La validación asegura que los valores asignados a los atributos cumplan con criterios específicos, lo que ayuda a mantener la integridad de tus datos.

En nuestra clase `Stock`, tenemos dos atributos importantes: `shares` y `price`. Queremos asegurarnos de que `shares` sea un entero no negativo y `price` sea un número de punto flotante no negativo. Para lograr esta validación, usaremos decoradores de propiedades junto con getters y setters.

## Instrucciones:

1. Primero, necesitas abrir el archivo `stock.py` en el editor. Aquí es donde realizaremos todos los cambios en nuestra clase `Stock`. Utiliza el siguiente comando en la terminal:

   ```bash
   code /home/labex/project/stock.py
   ```

2. En Python, podemos usar atributos privados para almacenar los valores reales de nuestras variables de clase. Los atributos privados se denotan con un guión bajo al principio. Agrega los atributos privados `_shares` y `_price` a la clase `Stock` y modifica el constructor para usarlos. El constructor es el método que se llama cuando creas una nueva instancia de la clase. Así es como se hace:

   ```python
   def __init__(self, name, shares, price):
       self.name = name
       self._shares = shares  # Using private attribute
       self._price = price    # Using private attribute
   ```

3. Ahora, definiremos propiedades para `shares` y `price` con una validación adecuada. Las propiedades se definen utilizando el decorador `@property` para el método getter y el decorador `@<property_name>.setter` para el método setter. El método getter se utiliza para recuperar el valor del atributo, y el método setter se utiliza para establecer el valor. Aquí está el código para agregar definiciones de propiedades con validación:

   ```python
   @property
   def shares(self):
       return self._shares

   @shares.setter
   def shares(self, value):
       if not isinstance(value, int):
           raise TypeError("Expected integer")
       if value < 0:
           raise ValueError("shares must be >= 0")
       self._shares = value

   @property
   def price(self):
       return self._price

   @price.setter
   def price(self, value):
       if not isinstance(value, float):
           raise TypeError("Expected float")
       if value < 0:
           raise ValueError("price must be >= 0")
       self._price = value
   ```

4. Actualiza el constructor para usar los setters de propiedades para la validación. De esta manera, cada vez que se crea una nueva instancia de la clase `Stock`, los valores de `shares` y `price` se validarán automáticamente. Aquí está el constructor actualizado:

   ```python
   def __init__(self, name, shares, price):
       self.name = name
       self.shares = shares  # Using property setter
       self.price = price    # Using property setter
   ```

5. Después de realizar todos estos cambios, guarda el archivo `stock.py`. Esto asegura que tus cambios se conserven.

6. Para verificar que nuestra validación funcione correctamente, crearemos un script de prueba. Abre un nuevo archivo llamado `test_validation.py` en el editor utilizando el siguiente comando:

   ```bash
   code /home/labex/project/test_validation.py
   ```

7. Agrega el siguiente código al archivo `test_validation.py`. Este código crea una instancia válida de `Stock` y luego intenta actualizar los atributos `shares` y `price` con valores válidos e inválidos. También imprime los resultados y cualquier mensaje de error que ocurra.

   ```python
   from stock import Stock

   # Create a valid stock instance
   s = Stock('GOOG', 100, 490.10)
   print(f"Initial: Name={s.name}, Shares={s.shares}, Price={s.price}, Cost={s.cost}")

   # Test valid updates
   try:
       s.shares = 50  # Valid update
       print(f"After setting shares=50: Shares={s.shares}, Cost={s.cost}")
   except Exception as e:
       print(f"Error setting shares=50: {e}")

   try:
       s.price = 123.45  # Valid update
       print(f"After setting price=123.45: Price={s.price}, Cost={s.cost}")
   except Exception as e:
       print(f"Error setting price=123.45: {e}")

   # Test invalid updates
   try:
       s.shares = "50"  # Invalid type (string)
       print("This line should not execute")
   except Exception as e:
       print(f"Error setting shares='50': {e}")

   try:
       s.shares = -10  # Invalid value (negative)
       print("This line should not execute")
   except Exception as e:
       print(f"Error setting shares=-10: {e}")

   try:
       s.price = "123.45"  # Invalid type (string)
       print("This line should not execute")
   except Exception as e:
       print(f"Error setting price='123.45': {e}")

   try:
       s.price = -10.0  # Invalid value (negative)
       print("This line should not execute")
   except Exception as e:
       print(f"Error setting price=-10.0: {e}")
   ```

8. Finalmente, ejecuta el script de prueba utilizando el siguiente comando en la terminal:
   ```bash
   python /home/labex/project/test_validation.py
   ```

Deberías ver una salida que muestre actualizaciones válidas exitosas y mensajes de error adecuados para actualizaciones inválidas. Esto confirma que nuestra validación de propiedades está funcionando como se espera.
