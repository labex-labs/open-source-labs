# Exercício 6.14: Expressões Geradoras em Argumentos de Função

Expressões geradoras são, às vezes, colocadas em argumentos de função. Parece um pouco estranho no início, mas tente este experimento:

```python
>>> nums = [1,2,3,4,5]
>>> sum([x*x for x in nums])    # A list comprehension
55
>>> sum(x*x for x in nums)      # A generator expression
55
>>>
```

No exemplo acima, a segunda versão usando geradores usaria significativamente menos memória se uma lista grande estivesse sendo manipulada.

No seu arquivo `portfolio.py`, você realizou alguns cálculos envolvendo compreensões de lista. Tente substituí-los por expressões geradoras.
