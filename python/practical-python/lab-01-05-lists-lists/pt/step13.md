# Exercício 1.25: Listas de qualquer coisa

Listas podem conter qualquer tipo de objeto, incluindo outras listas (por exemplo, listas aninhadas). Experimente:

```python
>>> nums = [101, 102, 103]
>>> items = ['spam', symlist, nums]
>>> items
['spam', ['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA'], [101, 102, 103]]
```

Preste muita atenção à saída acima. `items` é uma lista com três elementos. O primeiro elemento é uma string, mas os outros dois elementos são listas.

Você pode acessar itens nas listas aninhadas usando múltiplas operações de indexação.

```python
>>> items[0]
'spam'
>>> items[0][0]
's'
>>> items[1]
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>> items[1][1]
'RHT'
>>> items[1][1][2]
'T'
>>> items[2]
[101, 102, 103]
>>> items[2][1]
102
>>>
```

Embora seja tecnicamente possível criar estruturas de lista muito complicadas, como regra geral, é preferível manter as coisas simples. Normalmente, as listas contêm itens que são todos do mesmo tipo de valor. Por exemplo, uma lista que consiste inteiramente em números ou uma lista de strings de texto. Misturar diferentes tipos de dados na mesma lista é frequentemente uma boa maneira de fazer sua cabeça explodir, por isso é melhor evitar.
