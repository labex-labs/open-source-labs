# Herramientas de Prueba de Terceros

El módulo `unittest` integrado tiene la ventaja de estar disponible en todas partes: es parte de Python. Sin embargo, muchos programadores también lo encuentran bastante verboso. Una alternativa popular es [pytest](https://docs.pytest.org/en/latest/). Con pytest, tu archivo de prueba se simplifica a algo como lo siguiente:

```python
# test_simple.py
import simple

def test_simple():
    assert simple.add(2,2) == 4

def test_str():
    assert simple.add('hello','world') == 'helloworld'
```

Para ejecutar una prueba, simplemente escribe un comando como `python -m pytest`. Luego buscará y ejecutará todas las pruebas. El módulo se puede instalar usando `pip install pytest`.

Hay mucho más en `pytest` que este ejemplo, pero por lo general es bastante fácil de empezar si decides probarlo.

En este ejercicio, explorarás la mecánica básica de uso del módulo `unittest` de Python.

En ejercicios anteriores, escribiste un archivo `stock.py` que contenía una clase `Stock`. Para este ejercicio, se asumió que estás usando el código escrito para el Ejercicio 7.9 que involucra propiedades tipadas. Si, por alguna razón, eso no está funcionando, es posible que desees copiar la solución de `Soluciones/7_9` a tu directorio de trabajo.
