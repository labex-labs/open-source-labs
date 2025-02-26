# Ejercicio 8.1: Escribir Pruebas Unitarias

En un archivo separado `test_stock.py`, escribe un conjunto de pruebas unitarias para la clase `Stock`. Para ayudarte a empezar, aquí hay un pequeño fragmento de código que prueba la creación de instancias:

```python
# test_stock.py

import unittest
import stock

class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

if __name__ == '__main__':
    unittest.main()
```

Ejecuta tus pruebas unitarias. Deberías obtener una salida que se vea así:

## .

Ran 1 tests in 0.000s

    OK

Una vez que estés satisfecho de que funciona, escribe pruebas unitarias adicionales que comprueben lo siguiente:

- Asegúrate de que la propiedad `s.cost` devuelva el valor correcto (49010.0)
- Asegúrate de que el método `s.sell()` funcione correctamente. Debería decrementar el valor de `s.shares` en consecuencia.
- Asegúrate de que el atributo `s.shares` no se pueda establecer en un valor no entero.

Para la última parte, tendrás que comprobar que se lance una excepción. Una forma fácil de hacer eso es con código como este:

```python
class TestStock(unittest.TestCase):
  ...
    def test_bad_shares(self):
         s = stock.Stock('GOOG', 100, 490.1)
         with self.assertRaises(TypeError):
             s.shares = '100'
```
