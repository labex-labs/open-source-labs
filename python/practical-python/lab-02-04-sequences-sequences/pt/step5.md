# Iteração sobre uma sequência (Iteration over a sequence)

O laço for (for-loop) itera sobre os elementos em uma sequência.

```python
>>> s = [1, 4, 9, 16]
>>> for i in s:
...     print(i)
...
1
4
9
16
>>>
```

Em cada iteração do laço, você obtém um novo item para trabalhar. Este novo valor é colocado na variável de iteração. Neste exemplo, a variável de iteração é `x`:

```python
for x in s:         # `x` é uma variável de iteração
    ...statements
```

Em cada iteração, o valor anterior da variável de iteração é sobrescrito (se houver). Após o término do laço, a variável retém o último valor.
