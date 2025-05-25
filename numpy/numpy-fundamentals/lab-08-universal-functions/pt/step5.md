# Regras de _Type Casting_

O _type casting_ (conversão de tipos) é feito nas entradas de uma _ufunc_ quando não há uma implementação de _core loop_ (laço central) para os tipos de entrada fornecidos. As regras de _casting_ determinam quando um tipo de dado pode ser seguramente convertido para outro tipo de dado. Vamos ver um exemplo.

```python
import numpy as np

# Check if int can be safely cast to float
result = np.can_cast(np.int, np.float)

# Print the result
print(result)
```

Output:

```
True
```
