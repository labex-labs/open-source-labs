# Inicializar Lista com Range (Intervalo)

Escreva uma função `initialize_list_with_range(end, start=0, step=1)` que inicializa uma lista contendo os números no intervalo especificado, onde `start` e `end` são inclusivos com sua diferença comum `step`.

A função deve retornar uma lista com o comprimento apropriado, preenchida com os valores desejados no intervalo fornecido.

### Entrada

- `end` (inteiro) - O final do intervalo (inclusivo).
- `start` (inteiro, opcional) - O início do intervalo (inclusivo). O padrão é 0.
- `step` (inteiro, opcional) - A diferença comum entre cada número no intervalo. O padrão é 1.

### Saída

- Uma lista contendo os números no intervalo especificado.

```python
def initialize_list_with_range(end, start = 0, step = 1):
  return list(range(start, end + 1, step))
```

```python
initialize_list_with_range(5) # [0, 1, 2, 3, 4, 5]
initialize_list_with_range(7, 3) # [3, 4, 5, 6, 7]
initialize_list_with_range(9, 0, 2) # [0, 2, 4, 6, 8]
```
