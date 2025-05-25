# Exercício 2.20: Reduções de Sequência

Calcule o custo total do portfólio usando uma única instrução Python.

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> cost = sum([ s['shares'] * s['price'] for s in portfolio ])
>>> cost
44671.15
>>>
```

Depois de fazer isso, mostre como você pode calcular o valor atual do portfólio usando uma única instrução.

```python
>>> value = sum([ s['shares'] * prices[s['name']] for s in portfolio ])
>>> value
28686.1
>>>
```

Ambas as operações acima são um exemplo de map-reduction (mapeamento-redução). A compreensão de lista está mapeando uma operação em toda a lista.

```python
>>> [ s['shares'] * s['price'] for s in portfolio ]
[3220.0000000000005, 4555.0, 12516.0, 10246.0, 3835.1499999999996, 3254.9999999999995, 7044.0]
>>>
```

A função `sum()` então realiza uma redução em todo o resultado:

```python
>>> sum(_)
44671.15
>>>
```

Com este conhecimento, você está agora pronto para lançar uma empresa de startup de big data.
