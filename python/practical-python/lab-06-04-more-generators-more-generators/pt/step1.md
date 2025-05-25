# Expressões Geradoras (Generator Expressions)

Uma versão geradora de uma compreensão de lista (list comprehension).

```python
>>> a = [1,2,3,4]
>>> b = (2*x for x in a)
>>> b
<generator object at 0x58760>
>>> for i in b:
...   print(i, end=' ')
...
2 4 6 8
>>>
```

Diferenças em relação às Compreensões de Lista.

- Não constrói uma lista.
- Útil apenas para iteração.
- Uma vez consumida, não pode ser reutilizada.

Sintaxe geral.

```python
(<expressão> for i in s if <condicional>)
```

Também pode servir como um argumento de função.

```python
sum(x*x for x in a)
```

Pode ser aplicado a qualquer iterável (iterable).

```python
>>> a = [1,2,3,4]
>>> b = (x*x for x in a)
>>> c = (-x for x in b)
>>> for i in c:
...   print(i, end=' ')
...
-1 -4 -9 -16
>>>
```

O principal uso de expressões geradoras é em código que realiza algum cálculo em uma sequência, mas usa o resultado apenas uma vez. Por exemplo, remover todos os comentários de um arquivo.

```python
f = open('somefile.txt')
lines = (line for line in f if not line.startswith('#'))
for line in lines:
    ...
f.close()
```

Com geradores, o código roda mais rápido e usa pouca memória. É como um filtro aplicado a um fluxo (stream).
