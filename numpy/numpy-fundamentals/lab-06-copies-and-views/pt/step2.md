# Criando Visualizações (Views)

Visualizações podem ser criadas alterando certos metadados de um array. Isso cria uma nova maneira de olhar para os dados sem copiá-los. Para criar uma visualização, você pode usar o método `view()` do objeto `ndarray`.

```python
import numpy as np

# Criar um array
x = np.array([1, 2, 3, 4, 5])

# Criar uma visualização
y = x.view()

# Modificar a visualização
y[0] = 10

# Imprimir o array original
print(x)  # Output: [10, 2, 3, 4, 5]
```

No exemplo acima, a visualização `y` nos permite modificar o array original `x`.
