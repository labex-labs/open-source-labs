# Criando um Array Estruturado

Para criar um array estruturado, podemos usar a função `np.array` e especificar o tipo de dado (data type) usando o parâmetro `dtype`. O tipo de dado deve ser uma lista de tuplas, onde cada tupla representa um campo no array estruturado. Cada tupla deve conter o nome do campo e o tipo de dado do campo.

```python
import numpy as np

# Create a structured array
x = np.array([('Alice', 25), ('Bob', 30)], dtype=[('name', 'U10'), ('age', int)])
```
