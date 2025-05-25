# Criando novas listas

Uma list comprehension (compreensão de lista) cria uma nova lista aplicando uma operação a cada elemento de uma sequência.

```python
>>> a = [1, 2, 3, 4, 5]
>>> b = [2*x for x in a ]
>>> b
[2, 4, 6, 8, 10]
>>>
```

Outro exemplo:

```python
>>> names = ['Elwood', 'Jake']
>>> a = [name.lower() for name in names]
>>> a
['elwood', 'jake']
>>>
```

A sintaxe geral é: `[ <expressão> for <nome_da_variável> in <sequência> ]`.
