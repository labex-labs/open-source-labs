# Criando Cópias (Copies)

Cópias podem ser criadas duplicando tanto o buffer de dados quanto os metadados de um array. Para criar uma cópia, você pode usar o método `copy()` do objeto `ndarray`.

```python
import numpy as np

# Criar um array
x = np.array([1, 2, 3, 4, 5])

# Criar uma cópia
y = x.copy()

# Modificar a cópia
y[0] = 10

# Imprimir o array original
print(x)  # Output: [1, 2, 3, 4, 5]
```

No exemplo acima, a cópia `y` é independente do array original `x`.
