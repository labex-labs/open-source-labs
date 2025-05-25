# Exercício 6.13: Expressões Geradoras

Expressões geradoras são uma versão geradora de uma compreensão de lista (list comprehension). Por exemplo:

```python
>>> nums = [1, 2, 3, 4, 5]
>>> squares = (x*x for x in nums)
>>> squares
<generator object <genexpr> at 0x109207e60>
>>> for n in squares:
...     print(n)
...
1
4
9
16
25
```

Ao contrário de uma compreensão de lista, uma expressão geradora só pode ser usada uma vez. Portanto, se você tentar outro loop for, não obterá nada:

```python
>>> for n in squares:
...     print(n)
...
>>>
```
