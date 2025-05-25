# Fibonacci

Escreva uma função chamada `fibonacci(n)` que recebe um inteiro `n` como parâmetro e retorna uma lista contendo a sequência de Fibonacci até o n-ésimo termo.

Para resolver este problema, você pode seguir estes passos:

1. Crie uma lista vazia chamada `sequence`.
2. Se `n` for menor ou igual a 0, adicione 0 à lista `sequence` e retorne a lista.
3. Adicione 0 e 1 à lista `sequence`.
4. Use um loop `while` para adicionar a soma dos dois últimos números da lista `sequence` ao final da lista, até que o comprimento da lista atinja `n`.
5. Retorne a lista `sequence`.

```python
def fibonacci(n):
  if n <= 0:
    return [0]
  sequence = [0, 1]
  while len(sequence) <= n:
    next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
    sequence.append(next_value)
  return sequence
```

```python
fibonacci(7) # [0, 1, 1, 2, 3, 5, 8, 13]
```
