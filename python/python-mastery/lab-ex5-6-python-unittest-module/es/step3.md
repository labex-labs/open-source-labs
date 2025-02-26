# Pruebas unitarias con errores esperados

Supongamos que quieres escribir una prueba unitaria que verifique una excepción. Aquí está cómo se puede hacer:

```python
class TestStock(unittest.TestCase):
 ...
    def test_bad_shares(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
             s.shares = '50'
 ...
```

Usando esta prueba como guía, escribe pruebas unitarias para los siguientes modos de falla:

- Prueba que establecer `shares` en una cadena lance una `TypeError`.
- Prueba que establecer `shares` en un número negativo lance una `ValueError`.
- Prueba que establecer `price` en una cadena lance una `TypeError`.
- Prueba que establecer `price` en un número negativo lance una `ValueError`.
- Prueba que establecer un atributo no existente `share` lance una `AttributeError`.

En total, deberías tener alrededor de una docena de pruebas unitarias cuando termines.

**Nota importante**

Para usarlo más adelante en el curso, querrás tener un archivo `stock.py` y `teststock.py` completamente funcional. Guarda tu trabajo en progreso si es necesario, pero se te anima fuertemente a copiar el código de `Solutions/5_6` si las cosas todavía están rotas en este momento.

Vamos a usar el archivo `teststock.py` como una herramienta para mejorar el código de `Stock` más adelante. Querrás tenerlo a mano para asegurarte de que el nuevo código se comporte de la misma manera que el código antiguo.
