# Inicializar Lista com Valores

Escreva uma função `initialize_list_with_values(n, val=0)` que recebe dois parâmetros:

- `n` (inteiro) representando o comprimento da lista a ser criada.
- `val` (inteiro) representando o valor a ser usado para preencher a lista. Se `val` não for fornecido, o valor padrão de `0` deve ser usado.

A função deve retornar uma lista de comprimento `n` preenchida com o valor especificado.

```python
def initialize_list_with_values(n, val = 0):
  return [val for x in range(n)]
```

```python
initialize_list_with_values(5, 2) # [2, 2, 2, 2, 2]
```
