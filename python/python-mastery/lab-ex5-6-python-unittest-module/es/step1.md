# Creando tu primera prueba unitaria

El módulo `unittest` de Python es una herramienta poderosa que ofrece una forma estructurada de organizar y ejecutar pruebas. Antes de sumergirnos en la escritura de nuestra primera prueba unitaria, entendamos algunos conceptos clave. Los test fixtures son métodos como `setUp` y `tearDown` que ayudan a preparar el entorno antes de una prueba y limpiarlo después. Los casos de prueba (test cases) son unidades individuales de prueba, los conjuntos de pruebas (test suites) son colecciones de casos de prueba, y los ejecutores de pruebas (test runners) son responsables de ejecutar estas pruebas y presentar los resultados.

En este primer paso, vamos a crear un archivo de prueba básico para la clase `Stock`, que ya está definida en el archivo `stock.py`.

1. Primero, abramos el archivo `stock.py`. Esto nos ayudará a entender la clase `Stock` que vamos a probar. Al mirar el código en `stock.py`, podemos ver cómo está estructurada la clase, qué atributos tiene y qué métodos proporciona. Para ver el contenido del archivo `stock.py`, ejecuta el siguiente comando en tu terminal:

```bash
cat stock.py
```

2. Ahora, es el momento de crear un nuevo archivo llamado `teststock.py` utilizando tu editor de texto preferido. Este archivo contendrá nuestros casos de prueba para la clase `Stock`. Aquí está el código que debes escribir en el archivo `teststock.py`:

```python
# teststock.py

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

Desglosemos los componentes clave de este código:

- `import unittest`: Esta línea importa el módulo `unittest`, que proporciona las herramientas y clases necesarias para escribir y ejecutar pruebas en Python.
- `import stock`: Esto importa el módulo que contiene nuestra clase `Stock`. Sin esta importación, no podríamos acceder a la clase `Stock` en nuestro código de prueba.
- `class TestStock(unittest.TestCase)`: Creamos una nueva clase llamada `TestStock` que hereda de `unittest.TestCase`. Esto convierte nuestra clase `TestStock` en una clase de caso de prueba, que puede contener múltiples métodos de prueba.
- `def test_create(self)`: Este es un método de prueba. En el marco (framework) `unittest`, todos los métodos de prueba deben comenzar con el prefijo `test_`. Este método crea una instancia de la clase `Stock` y luego utiliza el método `assertEqual` para verificar si los atributos de la instancia de `Stock` coinciden con los valores esperados.
- `assertEqual`: Este es un método proporcionado por la clase `TestCase`. Verifica si dos valores son iguales. Si no son iguales, la prueba fallará.
- `unittest.main()`: Cuando se ejecuta este script directamente, `unittest.main()` ejecutará todos los métodos de prueba en la clase `TestStock` y mostrará los resultados.

3. Después de escribir el código en el archivo `teststock.py`, guárdalo. Luego, ejecuta el siguiente comando en tu terminal para ejecutar la prueba:

```bash
python3 teststock.py
```

Deberías ver una salida similar a esta:

```
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```

El punto único (`.`) en la salida indica que una prueba se ha pasado con éxito. Si una prueba falla, verás una `F` en lugar del punto, junto con información detallada sobre lo que salió mal en la prueba. Esta salida te ayuda a identificar rápidamente si tu código está funcionando como se espera o si hay algún problema que necesita ser solucionado.
