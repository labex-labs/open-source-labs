# Média de Lista Mapeada

Escreva uma função chamada `average_by(lst, fn = lambda x: x)` que recebe uma lista `lst` e uma função `fn` como argumentos. A função `fn` deve ser usada para mapear cada elemento da lista para um valor. A função deve então calcular a média dos valores mapeados e retorná-la.

Se o argumento `fn` não for fornecido, a função deve usar a função identidade padrão, que simplesmente retorna o próprio elemento.

Sua função deve atender aos seguintes requisitos:

- Use `map()` para mapear cada elemento para o valor retornado por `fn`.
- Use `sum()` para somar todos os valores mapeados, dividindo por `len(lst)`.
- Omita o último argumento, `fn`, para usar a função identidade padrão.

Assinatura da função: `def average_by(lst, fn = lambda x: x) -> float:`

```python
def average_by(lst, fn = lambda x: x):
  return sum(map(fn, lst), 0.0) / len(lst)
```

```python
average_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda x: x['n'])
# 5.0
```
