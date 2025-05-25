# Média Ponderada

Escreva uma função `weighted_average(nums, weights)` que recebe duas listas de mesmo comprimento: `nums` e `weights`. A função deve retornar a média ponderada dos números em `nums`, onde cada número é multiplicado pelo seu peso correspondente em `weights`. A média ponderada é calculada dividindo a soma dos produtos de cada número e seu peso pela soma dos pesos.

```python
def weighted_average(nums, weights):
  return sum(x * y for x, y in zip(nums, weights)) / sum(weights)
```

```python
weighted_average([1, 2, 3], [0.6, 0.2, 0.3]) # 1.72727
```
