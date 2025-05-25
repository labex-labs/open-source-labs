# Operações de Indexação (Indexing Operations)

As operações de indexação em NumPy podem criar visualizações (views) ou cópias (copies), dependendo do tipo de indexação.

- A indexação básica (basic indexing) sempre cria visualizações. Por exemplo:

```python
import numpy as np

# Criar um array
x = np.arange(10)

# Criar uma visualização
y = x[1:3]

# Modificar a visualização
y[0] = 10

# Imprimir o array original
print(x)  # Output: [0, 10, 2, 3, 4, 5, 6, 7, 8, 9]
```

No exemplo acima, a visualização `y` reflete as mudanças feitas no array original `x`.

- A indexação avançada (advanced indexing) sempre cria cópias. Por exemplo:

```python
import numpy as np

# Criar um array
x = np.arange(9).reshape(3, 3)

# Criar uma cópia
y = x[[1, 2]]

# Modificar o array original
x[[1, 2]] = [[10, 11, 12], [13, 14, 15]]

# Imprimir a cópia
print(y)  # Output: [[3, 4, 5], [6, 7, 8]]
```

No exemplo acima, a cópia `y` permanece inalterada após a modificação do array original `x`.
