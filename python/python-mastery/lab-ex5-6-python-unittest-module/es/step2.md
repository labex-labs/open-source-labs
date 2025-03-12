# Ampliar tus casos de prueba

Ahora que has creado un caso de prueba básico, es hora de ampliar el alcance de tus pruebas. Agregar más pruebas te ayudará a cubrir la funcionalidad restante de la clase `Stock`. De esta manera, puedes asegurarte de que todos los aspectos de la clase funcionen como se espera. Modificaremos la clase `TestStock` para incluir pruebas para varios métodos y propiedades.

1. Abre el archivo `teststock.py`. Dentro de la clase `TestStock`, vamos a agregar algunos nuevos métodos de prueba. Estos métodos probarán diferentes partes de la clase `Stock`. Aquí está el código que debes agregar:

```python
def test_create_keyword_args(self):
    s = stock.Stock(name='GOOG', shares=100, price=490.1)
    self.assertEqual(s.name, 'GOOG')
    self.assertEqual(s.shares, 100)
    self.assertEqual(s.price, 490.1)

def test_cost(self):
    s = stock.Stock('GOOG', 100, 490.1)
    self.assertEqual(s.cost, 49010.0)

def test_sell(self):
    s = stock.Stock('GOOG', 100, 490.1)
    s.sell(20)
    self.assertEqual(s.shares, 80)

def test_from_row(self):
    row = ['GOOG', '100', '490.1']
    s = stock.Stock.from_row(row)
    self.assertEqual(s.name, 'GOOG')
    self.assertEqual(s.shares, 100)
    self.assertEqual(s.price, 490.1)

def test_repr(self):
    s = stock.Stock('GOOG', 100, 490.1)
    self.assertEqual(repr(s), "Stock('GOOG', 100, 490.1)")

def test_eq(self):
    s1 = stock.Stock('GOOG', 100, 490.1)
    s2 = stock.Stock('GOOG', 100, 490.1)
    self.assertEqual(s1, s2)
```

Echemos un vistazo más de cerca a lo que hace cada una de estas pruebas:

- `test_create_keyword_args`: Esta prueba verifica si se puede crear un objeto `Stock` utilizando argumentos de palabra clave. Comprueba que los atributos del objeto se establecen correctamente.
- `test_cost`: Esta prueba verifica si la propiedad `cost` de un objeto `Stock` devuelve el valor correcto, que se calcula como el número de acciones multiplicado por el precio.
- `test_sell`: Esta prueba verifica si el método `sell()` de un objeto `Stock` actualiza correctamente el número de acciones después de vender algunas.
- `test_from_row`: Esta prueba verifica si el método de clase `from_row()` puede crear una nueva instancia de `Stock` a partir de una fila de datos.
- `test_repr`: Esta prueba verifica si el método `__repr__()` de un objeto `Stock` devuelve la representación de cadena esperada.
- `test_eq`: Esta prueba verifica si el método `__eq__()` compara correctamente dos objetos `Stock` para ver si son iguales.

2. Después de agregar estos métodos de prueba, guarda el archivo `teststock.py`. Luego, ejecuta las pruebas nuevamente utilizando el siguiente comando en tu terminal:

```bash
python3 teststock.py
```

Si todas las pruebas pasan, deberías ver una salida como esta:

```
......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```

Los siete puntos en la salida representan cada prueba. Cada punto indica que una prueba se ha pasado con éxito. Entonces, si ves siete puntos, significa que las siete pruebas han pasado.
