# Desafío de API: Pistas de Tipo

Las funciones pueden tener pistas opcionales de tipo adjuntas a los argumentos y a los valores de retorno. Por ejemplo:

```python
def add(x:int, y:int) -> int:
    return x + y
```

El módulo `typing` tiene clases adicionales para expresar tipos más complejos, incluyendo contenedores. Por ejemplo:

```python
from typing import List

def sum_squares(nums: List[int]) -> int:
    total = 0
    for n in nums:
        total += n*n
    return total
```

Su desafío: Modifique el código en `reader.py` de modo que todas las funciones tengan pistas de tipo. Intente hacer que las pistas de tipo sean lo más precisas posible. Para hacer esto, es posible que tenga que consultar la documentación del [módulo typing](https://docs.python.org/3/library/typing.html).
