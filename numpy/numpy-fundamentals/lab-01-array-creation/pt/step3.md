# Replicando, Juntando ou Mutando Arrays Existentes

Depois de criar arrays, você pode replicá-los, juntá-los ou mutá-los para criar novos arrays. Ao atribuir um array ou seus elementos a uma nova variável, use a função `np.copy` para criar um novo array em vez de uma view (visualização) do array original. Aqui está um exemplo:

```python
import numpy as np

# Create an array
a = np.array([1, 2, 3, 4])

# Create a view of the first two elements of the array
b = a[:2]

# Modify the view
b += 1

# Print the original array and the modified view
print('a =', a, '; b =', b)
```

Para juntar arrays, você pode usar funções como `np.vstack`, `np.hstack` e `np.block`. Aqui está um exemplo de como juntar quatro arrays 2x2 em um array 4x4 usando `np.block`:

```python
import numpy as np

A = np.ones((2, 2))
B = np.eye(2)
C = np.zeros((2, 2))
D = np.diag((-3, -4))

result = np.block([[A, B], [C, D]])
```
