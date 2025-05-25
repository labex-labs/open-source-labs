# Broadcasting com Arrays do Mesmo Formato

No caso mais simples, dois arrays devem ter exatamente o mesmo formato para operações elemento a elemento. Por exemplo:

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 2.0, 2.0])
result = a * b
```

Neste caso, `a` e `b` têm o mesmo formato, então a multiplicação é feita elemento a elemento e o resultado é `[2.0, 4.0, 6.0]`.
