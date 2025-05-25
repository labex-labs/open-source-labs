# Outras Operações (Other Operations)

Existem outras operações em NumPy que podem criar visualizações (views) ou cópias (copies).

- A função `reshape()` cria uma visualização (view) sempre que possível, ou uma cópia (copy) caso contrário. Por exemplo:

```python
import numpy as np

# Criar um array
x = np.ones((2, 3))

# Transpor o array
y = x.T

# Tentar remodelar o array
try:
    y.shape = 6
except AttributeError:
    print("Formato incompatível para modificação no local. Use `.reshape()` para fazer uma cópia com o formato desejado.")
```

No exemplo acima, o array `y` torna-se não-contíguo após a transposição, portanto, remodelá-lo requer uma cópia.

- A função `ravel()` retorna uma visualização (view) achatada e contígua do array sempre que possível. Por outro lado, o método `flatten()` sempre retorna uma cópia achatada do array. Por exemplo:

```python
import numpy as np

# Criar um array
x = np.arange(9).reshape(3, 3)

# Criar uma visualização achatada
y = x.ravel()

# Criar uma cópia achatada
z = x.flatten()

# Imprimir o array original
print(x)  # Output: [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
```

No exemplo acima, `y` é uma visualização (view), enquanto `z` é uma cópia (copy).
