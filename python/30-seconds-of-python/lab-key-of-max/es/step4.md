# Prueba del diccionario vacío (caso extremo)

Agreguemos una prueba específicamente para el caso del diccionario vacío. Agrega este método a tu clase `TestKeyOfMax` en `test_key_of_max.py`:

```python
    def test_empty_dictionary(self):
        self.assertIsNone(key_of_max({}))
```

- **`self.assertIsNone(...)`**: Esta afirmación (assertion) verifica si el valor es específicamente `None`. Esto es importante porque `self.assertEqual(..., None)` podría pasar para cosas que _se evalúan_ como `None`, pero en realidad no son `None`. `assertIsNone` es más estricto.

Ejecuta las pruebas nuevamente (`python3 test_key_of_max.py`). Las tres pruebas (las dos pruebas básicas y la prueba del diccionario vacío) ahora deberían pasar.

```python
python3 test_key_of_max.py
```

```plaintext
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```
