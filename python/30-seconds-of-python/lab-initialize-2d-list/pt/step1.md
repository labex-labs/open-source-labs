# Inicializar Lista 2D

Escreva uma função `initialize_2d_list(w, h, val=None)` que inicializa uma lista 2D com a largura, altura e valor dados. A função deve retornar uma lista de `h` linhas, onde cada linha é uma lista com comprimento `w`, inicializada com `val`. Se `val` não for fornecido, o valor padrão deve ser `None`.

```python
def initialize_2d_list(w, h, val = None):
  return [[val for x in range(w)] for y in range(h)]
```

```python
initialize_2d_list(2, 2, 0) # [[0, 0], [0, 0]]
```
