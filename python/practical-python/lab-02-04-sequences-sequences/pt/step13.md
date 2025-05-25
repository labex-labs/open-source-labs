# Exercício 2.14: Mais operações de sequência

Experimente interativamente algumas das operações de redução de sequência.

```python
>>> data = [4, 9, 1, 25, 16, 100, 49]
>>> min(data)
1
>>> max(data)
100
>>> sum(data)
204
>>>
```

Tente iterar sobre os dados.

```python
>>> for x in data:
        print(x)

4
9
...
>>> for n, x in enumerate(data):
        print(n, x)

0 4
1 9
2 1
...
>>>
```

Às vezes, a instrução `for`, `len()` e `range()` são usadas por iniciantes em algum tipo de fragmento de código horrível que parece ter emergido das profundezas de um programa C enferrujado.

```python
>>> for n in range(len(data)):
        print(data[n])

4
9
1
...
>>>
```

Não faça isso! Além de fazer os olhos de todos sangrarem ao ler, é ineficiente em termos de memória e roda muito mais lentamente. Apenas use um loop `for` normal se você quiser iterar sobre os dados. Use `enumerate()` se precisar do índice por algum motivo.
