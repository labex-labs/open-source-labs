# Soma de potências

Escreva uma função Python chamada `sum_of_powers` que recebe três parâmetros:

- `end` - um inteiro representando o fim do intervalo (inclusive)
- `power` - um inteiro representando a potência à qual cada número no intervalo deve ser elevado (o valor padrão é 2)
- `start` - um inteiro representando o início do intervalo (o valor padrão é 1)

A função deve retornar a soma das potências de todos os números de `start` a `end` (inclusive).

Para resolver este problema, você pode seguir estes passos:

1. Use `range()` em combinação com uma list comprehension (compreensão de lista) para criar uma lista de elementos no intervalo desejado elevados à `power` fornecida.
2. Use `sum()` para somar os valores.

```python
def sum_of_powers(end, power = 2, start = 1):
  return sum([(i) ** power for i in range(start, end + 1)])
```

```python
sum_of_powers(10) # 385
sum_of_powers(10, 3) # 3025
sum_of_powers(10, 3, 5) # 2925
```
