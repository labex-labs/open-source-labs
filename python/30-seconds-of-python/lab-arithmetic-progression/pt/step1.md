# Progressão Aritmética

Escreva uma função `arithmetic_progression(n, lim)` que recebe dois inteiros positivos `n` e `lim` e retorna uma lista de números na progressão aritmética, começando com `n` e indo até `lim`. A função deve usar `range()` e `list()` com os valores apropriados de início (start), passo (step) e fim (end) para gerar a lista.

### Entrada

- Dois inteiros positivos `n` e `lim`, onde `n` é o número inicial e `lim` é o limite.

### Saída

- Uma lista de números na progressão aritmética, começando com `n` e indo até `lim`.

```python
def arithmetic_progression(n, lim):
  return list(range(n, lim + 1, n))
```

```python
arithmetic_progression(5, 25) # [5, 10, 15, 20, 25]
```
