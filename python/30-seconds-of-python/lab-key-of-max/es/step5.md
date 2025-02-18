# Prueba con valores negativos

Como prueba final, manejemos un caso en el que todos los valores en el diccionario son negativos. Agrega este método a `TestKeyOfMax`:

```python
    def test_all_negative_values(self):
        self.assertEqual(key_of_max({'x': -5, 'y': -2, 'z': -10}), 'y')
```

Esta prueba asegura que nuestra función identifique correctamente el valor _menos negativo_ (que es el máximo en este caso) y devuelva su clave asociada.

Ejecuta tus pruebas una última vez (`python3 test_key_of_max.py`). Las cuatro pruebas deben pasar. Esto nos da una alta confianza de que nuestra función está funcionando correctamente.

Tu archivo `test_key_of_max.py` completo ahora debería verse así:

```python
import unittest
from key_of_max import key_of_max

class TestKeyOfMax(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(key_of_max({'a': 4, 'b': 0, 'c': 13}), 'c')

    def test_another_case(self):
        self.assertEqual(key_of_max({'apple': 10, 'banana': 5, 'orange': 10}), 'apple')

    def test_empty_dictionary(self):
        self.assertIsNone(key_of_max({}))

    def test_all_negative_values(self):
        self.assertEqual(key_of_max({'x': -5, 'y': -2, 'z': -10}), 'y')

if __name__ == '__main__':
    unittest.main()
```

Ejecuta las pruebas nuevamente (`python3 test_key_of_max.py`). Las cuatro pruebas deben pasar. Esto nos da una alta confianza de que nuestra función está funcionando correctamente.

```python
python3 test_key_of_max.py
```

```plaintext
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```
