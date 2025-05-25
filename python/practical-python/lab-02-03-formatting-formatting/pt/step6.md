# Exercício 2.8: Como formatar números

Um problema comum ao imprimir números é especificar o número de casas decimais. Uma maneira de corrigir isso é usar f-strings. Experimente estes exemplos:

```python
>>> value = 42863.1
>>> print(value)
42863.1
>>> print(f'{value:0.4f}')
42863.1000
>>> print(f'{value:>16.2f}')
        42863.10
>>> print(f'{value:<16.2f}')
42863.10
>>> print(f'{value:*>16,.2f}')
*******42,863.10
>>>
```

A documentação completa sobre os códigos de formatação usados em f-strings pode ser encontrada [aqui](https://docs.python.org/3/library/string.html#format-specification-mini-language). A formatação também é, por vezes, realizada usando o operador `%` de strings.

```python
>>> print('%0.4f' % value)
42863.1000
>>> print('%16.2f' % value)
        42863.10
>>>
```

A documentação sobre vários códigos usados com `%` pode ser encontrada [aqui](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting).

Embora seja comumente usado com `print`, a formatação de strings não está ligada à impressão. Se você quiser salvar uma string formatada, basta atribuí-la a uma variável.

```python
>>> f = '%0.4f' % value
>>> f
'42863.1000'
>>>
```
