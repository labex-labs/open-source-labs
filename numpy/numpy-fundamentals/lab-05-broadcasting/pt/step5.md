# Exemplos de Broadcasting

Vamos analisar alguns exemplos para entender como o broadcasting (difusão) funciona em diferentes cenários.

- Exemplo 1:

```python
import numpy as np

a = np.array([[1.0, 2.0, 3.0],
              [4.0, 5.0, 6.0]])
b = np.array([1.0, 2.0, 3.0])
result = a + b
```

Neste caso, `b` é adicionado a cada linha de `a`. O resultado é um array 2D com o mesmo formato de `a`, onde cada elemento é a soma dos elementos correspondentes em `a` e `b`.

- Exemplo 2:

```python
import numpy as np

a = np.array([[1.0, 2.0, 3.0],
              [4.0, 5.0, 6.0]])
b = np.array([1.0, 2.0])
result = a + b
```

Neste caso, o broadcasting falha porque as dimensões finais de `a` e `b` não são iguais. É impossível alinhar os valores nas linhas de `a` com os elementos de `b` para a adição elemento a elemento.
