# Exercício 7.6: Ordenando por um campo com lambda

Tente ordenar o portfólio de acordo com o número de ações usando uma expressão `lambda`:

```python
>>> portfolio.sort(key=lambda s: s.shares)
>>> for s in portfolio:
        print(s)

... inspecione o resultado ...
>>>
```

Tente ordenar o portfólio de acordo com o preço de cada ação

```python
>>> portfolio.sort(key=lambda s: s.price)
>>> for s in portfolio:
        print(s)

... inspecione o resultado ...
>>>
```

Observação: `lambda` é um atalho útil porque permite definir uma função de processamento especial diretamente na chamada para `sort()` em vez de ter que definir uma função separada primeiro.
