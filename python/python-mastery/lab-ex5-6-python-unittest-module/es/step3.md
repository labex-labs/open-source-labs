# Pruebas de excepciones

Las pruebas son una parte crucial del desarrollo de software, y un aspecto importante de ellas es garantizar que tu código pueda manejar adecuadamente las condiciones de error. En Python, el módulo `unittest` proporciona una forma conveniente de probar si se generan excepciones específicas como se espera.

1. Abre el archivo `teststock.py`. Vamos a agregar algunos métodos de prueba diseñados para comprobar si se generan excepciones. Estas pruebas nos ayudarán a asegurarnos de que nuestro código se comporta correctamente cuando encuentra una entrada no válida.

```python
def test_shares_type(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(TypeError):
        s.shares = '50'

def test_shares_value(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(ValueError):
        s.shares = -50

def test_price_type(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(TypeError):
        s.price = '490.1'

def test_price_value(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(ValueError):
        s.price = -490.1

def test_attribute_error(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(AttributeError):
        s.share = 100  # 'share' is incorrect, should be 'shares'
```

Ahora, entendamos cómo funcionan estas pruebas de excepciones.

- La declaración `with self.assertRaises(ExceptionType):` crea un gestor de contexto (context manager). Este gestor de contexto comprueba si el código dentro del bloque `with` genera la excepción especificada.
- Si se genera la excepción esperada dentro del bloque `with`, la prueba pasa. Esto significa que nuestro código está detectando correctamente la entrada no válida y generando el error adecuado.
- Si no se genera ninguna excepción o se genera una excepción diferente, la prueba falla. Esto indica que nuestro código puede no estar manejando la entrada no válida como se espera.

Estas pruebas están diseñadas para verificar los siguientes escenarios:

- Establecer el atributo `shares` a una cadena debe generar un `TypeError` porque `shares` debe ser un número.
- Establecer el atributo `shares` a un número negativo debe generar un `ValueError` ya que el número de acciones no puede ser negativo.
- Establecer el atributo `price` a una cadena debe generar un `TypeError` porque `price` debe ser un número.
- Establecer el atributo `price` a un número negativo debe generar un `ValueError` ya que el precio no puede ser negativo.
- Intentar establecer un atributo inexistente `share` (observa la falta de la 's') debe generar un `AttributeError` porque el nombre correcto del atributo es `shares`.

2. Después de agregar estos métodos de prueba, guarda el archivo `teststock.py`. Luego, ejecuta todas las pruebas utilizando el siguiente comando en tu terminal:

```bash
python3 teststock.py
```

Si todo está funcionando correctamente, deberías ver una salida que indique que las 12 pruebas se han pasado. La salida se verá así:

```
............
----------------------------------------------------------------------
Ran 12 tests in 0.002s

OK
```

Los doce puntos representan todas las pruebas que has escrito hasta ahora. Había 7 pruebas del paso anterior, y acabamos de agregar 5 nuevas. Esta salida muestra que tu código está manejando las excepciones como se espera, lo cual es una gran señal de un programa bien probado.
