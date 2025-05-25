# Exercício 7.5: Ordenando por um campo

Experimente as seguintes declarações que ordenam os dados do portfólio alfabeticamente pelo nome da ação.

```python
>>> def stock_name(s):
       return s.name

>>> portfolio.sort(key=stock_name)
>>> for s in portfolio:
           print(s)

... inspecione o resultado ...
>>>
```

Nesta parte, a função `stock_name()` extrai o nome de uma ação de uma única entrada na lista `portfolio`. `sort()` usa o resultado desta função para fazer a comparação.
