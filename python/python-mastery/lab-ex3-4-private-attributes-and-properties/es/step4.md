# Uso de `__slots__` para la Optimización de Memoria

En Python, el atributo `__slots__` es una herramienta especial que puede ayudarte a gestionar tus clases de manera más eficiente. Restringe los atributos que una clase puede tener. Normalmente, Python almacena los atributos de instancia en un diccionario llamado `__dict__`, lo que permite la adición dinámica de nuevos atributos. Sin embargo, cuando defines `__slots__`, Python crea una estructura estática para las instancias. Esto tiene dos efectos principales: impide la adición de nuevos atributos a las instancias y reduce el uso de memoria porque no es necesario mantener el `__dict__`.

En nuestra clase `Stock`, usaremos `__slots__` por dos razones importantes:

1. Para restringir la creación de atributos solo a los atributos que hemos definido. Esto significa que los usuarios de la clase no pueden agregar accidentalmente o intencionalmente nuevos atributos que no hayamos planeado.
2. Para mejorar la eficiencia de memoria, especialmente cuando se crean muchas instancias. Si tienes una gran cantidad de objetos de la clase `Stock`, el uso de `__slots__` puede ahorrar una cantidad significativa de memoria.

## Instrucciones:

1. Primero, necesitas abrir el archivo `stock.py` en el editor. Aquí es donde realizaremos cambios en la clase `Stock`. Utiliza el siguiente comando en la terminal:

   ```bash
   code /home/labex/project/stock.py
   ```

2. Dentro del archivo `stock.py`, agregaremos una variable de clase `__slots__`. Esta variable debe enumerar todos los nombres de atributos privados utilizados por la clase. Así es como se hace:

   ```python
   class Stock:
       # Class variable for type conversions
       _types = (str, int, float)

       # Define slots to restrict attribute creation
       __slots__ = ('name', '_shares', '_price')

       # Rest of the class...
   ```

   Al definir `__slots__` de esta manera, le estamos diciendo a Python que las instancias de la clase `Stock` solo pueden tener los atributos `name`, `_shares` y `_price`.

3. Después de realizar estos cambios, guarda el archivo. Esto asegura que tus modificaciones se conserven.

4. Ahora, necesitamos crear un script de prueba para verificar que `__slots__` está funcionando como se espera. Abre un nuevo archivo llamado `test_slots.py` utilizando el siguiente comando:

   ```bash
   code /home/labex/project/test_slots.py
   ```

5. Agrega el siguiente código al archivo `test_slots.py`. Este código creará una instancia de la clase `Stock`, accederá a sus atributos existentes y luego intentará agregar un nuevo atributo.

   ```python
   from stock import Stock

   # Create a stock instance
   s = Stock('GOOG', 100, 490.10)

   # Access existing attributes
   print(f"Name: {s.name}")
   print(f"Shares: {s.shares}")
   print(f"Price: {s.price}")
   print(f"Cost: {s.cost}")

   # Try to add a new attribute
   try:
       s.extra = "This will fail"
       print(f"Extra: {s.extra}")
   except AttributeError as e:
       print(f"Error: {e}")
   ```

   El bloque `try` intenta agregar un nuevo atributo `extra` a la instancia `s` de `Stock`. Si `__slots__` está funcionando correctamente, esto debería generar un `AttributeError` porque `extra` no está enumerado en `__slots__`.

6. Finalmente, ejecuta el script de prueba utilizando el siguiente comando:
   ```bash
   python /home/labex/project/test_slots.py
   ```

Deberías ver una salida que muestre que puedes acceder a los atributos definidos, pero intentar agregar un nuevo atributo genera un `AttributeError`. Esto confirma que `__slots__` está funcionando como se pretendía.

### Comprendiendo `__slots__`

Al usar `__slots__`, es importante tener en cuenta los siguientes puntos:

1. Debes enumerar todos los atributos que se almacenarán en la instancia. Si olvidas enumerar un atributo, no podrás asignarlo a la instancia.
2. Solo los atributos enumerados en `__slots__` se pueden asignar a las instancias. Esto ayuda a imponer una estructura estricta para tus objetos.
3. Las instancias ya no tendrán un atributo `__dict__`. Dado que `__slots__` crea una estructura estática, no es necesario el diccionario dinámico.
4. Las subclases no heredarán los `__slots__` de su clase padre a menos que definan sus propios `__slots__`. Esto significa que las subclases tienen la flexibilidad de definir sus propias restricciones de atributos.

Los principales beneficios de usar `__slots__` son:

1. **Eficiencia de memoria**: Las instancias utilizan menos memoria porque no hay un `__dict__` para almacenar atributos.
2. **Velocidad**: El acceso a atributos es ligeramente más rápido porque Python no necesita buscar el atributo en un diccionario.
3. **Prevención de la creación accidental de atributos**: Ayuda a detectar errores tipográficos y de programación al impedir la adición de atributos inesperados.
