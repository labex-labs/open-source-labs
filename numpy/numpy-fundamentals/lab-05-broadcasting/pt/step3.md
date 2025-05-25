# Broadcasting com um Valor Escalar

O broadcasting (difusão) também permite operações elemento a elemento entre um array e um valor escalar. O valor escalar é automaticamente "estendido" para corresponder ao formato do array. Por exemplo:

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = 2.0
result = a * b
```

Neste caso, `b` é um valor escalar, mas ele é estendido para se tornar um array com o mesmo formato de `a`. A multiplicação é então feita elemento a elemento, resultando em `[2.0, 4.0, 6.0]`.
