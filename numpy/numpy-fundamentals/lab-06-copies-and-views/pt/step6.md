# Determinando se um Array é uma Visualização (View) ou uma Cópia (Copy)

Você pode usar o atributo `base` do objeto `ndarray` para determinar se um array é uma visualização (view) ou uma cópia (copy). O atributo `base` retorna o array original para uma visualização e `None` para uma cópia. Por exemplo:

```python
import numpy as np

# Criar um array
x = np.arange(9)

# Criar uma visualização
y = x.reshape(3, 3)

# Criar uma cópia
z = y[[2, 1]]

# Verificar se y é uma visualização
print(y.base)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Verificar se z é uma cópia
print(z.base is None)  # Output: True
```

No exemplo acima, `y` é uma visualização (view) e `z` é uma cópia (copy).
