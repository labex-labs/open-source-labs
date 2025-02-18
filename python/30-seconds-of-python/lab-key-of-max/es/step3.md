# Creación de pruebas unitarias: Pruebas básicas

Ahora, escribamos algunas pruebas para asegurarnos de que nuestra función funcione correctamente. Usaremos el módulo `unittest` de Python. Crea un nuevo archivo llamado `test_key_of_max.py` y agrega el siguiente código:

```python
import unittest
from key_of_max import key_of_max  # Import our function

class TestKeyOfMax(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(key_of_max({'a': 4, 'b': 0, 'c': 13}), 'c')

    def test_another_case(self):
        self.assertEqual(key_of_max({'apple': 10, 'banana': 5, 'orange': 10}), 'apple')

if __name__ == '__main__':
    unittest.main()
```

Explicación:

1.  **`import unittest`**: Importa el marco de pruebas (testing framework).
2.  **`from key_of_max import key_of_max`**: Importa la función que queremos probar.
3.  **`class TestKeyOfMax(unittest.TestCase):`**: Define una _clase de prueba_. Las clases de prueba agrupan pruebas relacionadas.
4.  **`def test_basic_case(self):`**: Define un _método de prueba_. Cada método de prueba verifica un aspecto específico de nuestra función. Los nombres de los métodos de prueba _deben_ comenzar con `test_`.
5.  **`self.assertEqual(...)`**: Esta es una _afirmación_ (assertion). Verifica si dos valores son iguales. Si no son iguales, la prueba falla. En este caso, estamos verificando si `key_of_max({'a': 4, 'b': 0, 'c': 13})` devuelve `'c'`, lo cual debería ser así.
6.  **`def test_another_case(self):`**: Se agregó otro caso de prueba para verificar la clave del valor máximo, que puede no ser única.
7.  **`if __name__ == '__main__': unittest.main()`**: Este es un patrón estándar de Python que ejecuta las pruebas cuando se ejecuta el script directamente (por ejemplo, `python3 test_key_of_max.py`).

Ejecuta las pruebas desde tu terminal: `python3 test_key_of_max.py`. Deberías ver una salida que indique que las dos pruebas pasaron.

```python
python3 test_key_of_max.py
```

```plaintext
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
