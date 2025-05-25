# Digitize Number (Digitalizar Número)

Escreva uma função `digitize(n)` que recebe um inteiro não negativo `n` como entrada e retorna uma lista de seus dígitos. A função deve realizar isso executando as seguintes etapas:

1.  Converter o número de entrada `n` em uma string.
2.  Usar a função `map()` combinada com a função `int` para converter cada caractere na string em um inteiro.
3.  Retornar a lista resultante de inteiros.

Por exemplo, se o número de entrada for `123`, a função deve retornar a lista `[1, 2, 3]`.

```python
def digitize(n):
  return list(map(int, str(n)))
```

```python
digitize(123) # [1, 2, 3]
```
