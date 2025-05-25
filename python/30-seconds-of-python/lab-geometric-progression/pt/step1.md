# Progressão Geométrica (Geometric Progression)

Escreva uma função chamada `geometric_progression` que recebe três parâmetros:

- `end`: um inteiro representando o final do intervalo (inclusivo)
- `start`: um inteiro opcional representando o início do intervalo (inclusivo), com um valor padrão de `1`
- `step`: um inteiro opcional representando a razão comum (common ratio) entre dois termos, com um valor padrão de `2`

A função deve retornar uma lista contendo os números no intervalo especificado, onde a razão entre dois termos é `step`. A lista deve começar com `start` e terminar com `end`.

Se `step` for igual a `1`, a função deve retornar um erro.

Você deve usar `range()`, `math.log()` e `math.floor()` e uma list comprehension para criar uma lista do comprimento apropriado, aplicando o passo (step) para cada elemento.

```python
from math import floor, log

def geometric_progression(end, start=1, step=2):
  return [start * step ** i for i in range(floor(log(end / start)
          / log(step)) + 1)]
```

```python
geometric_progression(256) # [1, 2, 4, 8, 16, 32, 64, 128, 256]
geometric_progression(256, 3) # [3, 6, 12, 24, 48, 96, 192]
geometric_progression(256, 1, 4) # [1, 4, 16, 64, 256]
```
